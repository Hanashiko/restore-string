from typing import List

def restoreString(s: str, indices: List[int]) -> str:
    length_of_string: int = len(s)
    result_list: List[str] = [str("") for _ in range(length_of_string)]
    for i in range(length_of_string):
        result_list[i] = s[indices.index(i)]
    return "".join(result_list)

def main() -> None:
    print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))
    print(restoreString("abc", [0,1,2]))
    
if __name__ == "__main__":
    main()