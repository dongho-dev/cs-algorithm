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

- `rstrip('\n')`만 호출하므로 앞·뒤 공백(스페이스, 탭)은 **그대로 유지**.  
- 대량 입력에서는 `.readline()`만 사용하는 것이 불필요한 오버헤드를 줄여 **속도** 면에서 유리함.

--- 

## sys.stdin.readline() 동작 원리