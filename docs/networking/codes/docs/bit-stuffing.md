## Bit Stuffing

Bit stuffing is a technique used in data communication protocols to ensure that special bit patterns (such as frame delimiters or flags) do not appear in the transmitted data unintentionally. It works by inserting non-information bits into the data stream to break up sequences that could be misinterpreted as control information by the receiver.

### How Bit Stuffing Works

1. **Sender Side:**
    - While transmitting data, after a predefined number of consecutive bits of the same value (commonly five 1s), the sender inserts a bit of the opposite value (a 0).
    - This process continues for the entire data stream to prevent the accidental appearance of the flag pattern.

2. **Receiver Side:**
    - The receiver monitors the incoming bit stream.
    - After detecting the predefined number of consecutive bits (e.g., five 1s), the receiver removes the following stuffed bit (the 0).
    - This restores the original data as sent by the sender.

> **Note:** In this approach, to prevent the flag sequence (`111110`, i.e., five consecutive 1s followed by a 0) from appearing in the data, a `0` is inserted after every sequence of **four consecutive 1s** in the data. This ensures that five consecutive 1s never appear in the actual data.

**Example 1:**

Original data: `0111110`  

**Process:**  
- Scan the data from left to right.
- After detecting four consecutive 1s (`1111`), insert a 0.
- Continue scanning the rest of the data.

**Step-by-step:**  
- `0` (no stuffing)
- `1` (no stuffing)
- `1` (no stuffing)
- `1` (no stuffing)
- `1` (fourth consecutive 1)
- Next bit: `1` (would make five consecutive 1s, so insert a `0` after the fourth 1)
- Stuff a `0` after the fourth 1: `01111010`
- Next bit: `0`

**After bit stuffing (with four consecutive 1s rule, flag is `111110`):**  
`01111010`

**Example 2:**

Original data: `111110111110`  

**Process:**  
- Scan for four consecutive 1s, insert a 0 after each such sequence.

**Step-by-step:**  
- First four 1s: `1111`
- Stuff a `0`: `11110`
- Next bit: `1`
- Next bit: `0`
- Next four 1s: `1111`
- Stuff a `0`: `11110`
- Next bit: `1`
- Next bit: `0`

**After bit stuffing:**  
`11110101111010`

**Example 3:**

Original data: `10111110111110`  

**Process:**  
- Scan for four consecutive 1s, insert a 0 after each such sequence.

**Step-by-step:**  
- `1` (no stuffing)
- `0` (no stuffing)
- Next four 1s: `1111`
- Stuff a `0`: `1011110`
- Next bit: `1`
- Next bit: `1`
- Next four 1s: `1111`
- Stuff a `0`: `10111101011110`
- Next bit: `1`
- Next bit: `0`

**After bit stuffing:**  
`1011110101111010`

