def test_awk():
    time,count={},{}
    data=[["a",1],
        ["a",2],
        ["a",3],
        ["b",4],
        ["b",5],
        ["b",6]]
    for record in data:
        time.setdefault(record[0],0)
        time[record[0]]+=record[1]
        count.setdefault(record[0],0)
        count[record[0]]+=1
    for k in time:
        print(f"k={k},avg={time[k]/count[k]}")

if __name__ == '__main__':
    test_awk()