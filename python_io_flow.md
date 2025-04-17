# I/O 버퍼링 & Python 입출력 흐름

## input() vs `sys.stdin.readline()`

### `input()`

Python의 `input()`은 내부적으로 다음과 같이 동작함.

```python
line = sys.stdin.readline()      # 실제로 이것을 호출
if not line:
    raise EOFError
return line.rstrip('\n')         # 오른쪽 끝의 개행문자만 제거
```
v
- `rstrip('\n')`만 호출하므로 앞·뒤 공백(스페이스, 탭)은 **그대로 유지**.  
- 대량 입력에서는 `sys.stdin.readline()`만 사용하는 것이 불필요한 오버헤드를 줄여 **속도** 면에서 유리함.

--- 

## sys.stdin.readline() 동작 원리

## 🔁 전체 흐름 개요

```bash
Python code
  ↓
TextIOWrapper.readline()           ←─ Modules/_io/textio.c
  ↓
BufferedReader.read1()             ←─ Modules/_io/bufferedio.c
  ↓
FileIO.read()                      ←─ Modules/_io/fileio.c
  ↓
read(fd, buf, size) system call   ←─ libc (glibc/musl)
  ↓                                     커널 페이지 캐시 / 파이프 버퍼
bytes 반환                           
  ↑
FileIO.read() returns bytes        
  ↑
BufferedReader.read1() returns bytes
  ↑
TextIOWrapper.readline() decodes → str
  ↑
Python receives str
```

---

## 1️⃣ Python 레벨: `sys.stdin.readline()`

```python
line = sys.stdin.readline()
```

- 사용자가 `sys.stdin.readline()` 호출
- Python 인터프리터는 `sys` 모듈의 `stdin` 속성을 찾아서, 이미 만들어져 있는 `TextIOWrapper` 객체를 반환
- 이 객체의 `readline()` 호출 → 내부적으로 C 함수 `textiowrapper_readline()` 실행됨

---

## 2️⃣ TextIOWrapper (텍스트 레이어)

- **파일**: `Modules/_io/textio.c`  
- **함수**: `textiowrapper_readline(textio, sizehint)`

### 하는 일:

- 내부적으로 `_textiowrapper_read_chunks()` 호출해서 바이트 청크 반복 수집
- 하위 `buffer.read1()` 호출로부터 바이트 수급
- 모은 바이트 덩어리에 `UTF‑8` 디코딩 수행 → Python `str` 생성
- `\n` 포함된 문자열을 완성해서 반환

> 🧑‍🍳 비유: 텍스트 셰프가 바이트 재료를 조리(디코딩)해서 문자열 요리를 내놓는 단계

---

## 3️⃣ BufferedReader (버퍼링 레이어)

- **파일**: `Modules/_io/bufferedio.c`  
- **함수**: `bufferedreader_read1(buffered, size)`

### 하는 일:

- 내부 힙 버퍼에 읽을 데이터 충분한지 확인
- 부족하면 `bufferedreader_fill()` 호출 → `raw.read()`로부터 바이트 채움
- 내부 버퍼에서 필요한 만큼 슬라이스로 꺼내서 Python `bytes` 객체로 반환

> 🧑‍🏭 비유: 마트 점원이 창고에서 대량으로 들여온 물건을 선반에 채워두고, 손님이 요청한 만큼씩 꺼내주는 단계

---

## 4️⃣ FileIO (Raw I/O 레이어)

- **파일**: `Modules/_io/fileio.c`  
- **함수**: `fileio_read(fileio, size)`

### 하는 일:

- Python 바이트 객체를 미리 할당 (`PyBytes_FromStringAndSize`)
- `_fileio_read()` → 실제 시스템 콜 `read(fd, buf, size)` 호출
- 커널이 페이지 캐시나 파이프 버퍼에서 유저 공간으로 바이트 복사
- Python 바이트 객체로 반환

> 🚚 비유: 매장의 출고 담당자가 트럭(시스템콜)을 호출해 도매 창고(커널)에서 재고를 실어오는 단계

---

## 5️⃣ libc & 커널

### libc (glibc/musl):

- `read()` 시스템 콜 인터페이스 제공
- 유저 공간에 있는 버퍼로 커널 페이지 캐시/파이프 버퍼 내용을 복사 (`copy_to_user()`)

### 커널:

- **정규 파일**: 디스크 → 페이지 캐시 → `read()` → 유저 버퍼  
- **파이프/터미널**: 커널 pipe buffer → `read()` → 유저 버퍼

> 🧠 시스템콜의 반환값은 실제 읽은 바이트 수. libc가 이걸 받아서 Python 레이어로 전달하는 거지.

---

## 🧩 논리적 연결 요약

- **Python → TextIOWrapper**:  
  Python 코드에서 C 함수 포인터(`textiowrapper_readline`) 호출로 넘어가는 첫 관문

- **Text → Buffered**:  
  텍스트 셰프가 바이트 청크를 받기 위해 `buffer.read1()` 호출

- **Buffered → FileIO**:  
  내부 버퍼가 부족하면 raw IO 레이어로 하강, 실제 데이터 수급

- **FileIO → OS read()**:  
  시스템 콜로 커널의 창고(페이지 캐시 or 파이프)에서 데이터를 복사해오는 단계

---

## 🔁 데이터 반환 역순 흐름

```text
커널
  ↓
libc
  ↓
FileIO
  ↓
BufferedReader
  ↓
TextIOWrapper
  ↓
Python 코드에서 str로 수신
```
