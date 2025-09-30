## stack-chess

This is a demonstration of a custom chess variant ("Stack Chess").

# Rules
Most rules of Stack Chess are identical to those of regular chess. The key difference is the addition of **Stacks**.
- Stacks consist of multiple pieces of the same color occupying the same square.
- A stack can move to any square in which one of its component pieces has a legal move to it.
- - An exception occurs when the stack contains a king, in which it behaves exactly like a king.
- If captured, all pieces within the stack are captured at the same time.
- A piece can be removed from the stack by moving by itself out of the stack's square, but only one piece may be removed at a time.
- Pawns in stacks do not promote if on the eight rack.

All code in this repository is written in python for the pygame library.

created c. June 2022 by Kenneth Ren and Alexander Tian
