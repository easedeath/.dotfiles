Vim�UnDo� L�*i�
(�.L�U��i�
�Vl12PҦ
f�   n                                   a��    _�                      l        ����                                                                                                                                                                                                                                                                                                                                                             a��    �   l            �   k   m              solve()�   j   l          for _ in " " * ii():�   i   k           �   h   j          !    print(B if c % 2 == 0 else A)�   g   i           �   f   h              # print(c)�   e   g              c //= 2�   d   f              c -= c % 2�   c   e           �   b   d                  c += arr[i] == arr[i+1]�   a   c              for i in range(n - 1):�   `   b           �   _   a          	    c = 0�   ^   `           �   ]   _                  return�   \   ^                      print(B)�   [   ]                  else:�   Z   \                      print(A)�   Y   [                  if arr[0] == arr[1]:�   X   Z              if n == 2:�   W   Y           �   V   X                  return�   U   W                  print(B)�   T   V              if n == 1:�   S   U           �   R   T              arr = list(input())�   Q   S              n = ii()�   P   R          def solve():�   O   Q           �   N   P          
B = "Uttu"�   M   O          A = "JJ"�   L   N           �   K   M          # --------------------------�   J   L           �   I   K           �   H   J          rr = lambda: list(r())�   G   I          %r = lambda: map(int, input().split())�   F   H          ii = lambda: int(input())�   E   G           �   D   F           �   C   E          %ceil_ = lambda a, b: (a + b - 1) // b�   B   D          !en = lambda x: list(enumerate(x))�   A   C          inf = float("inf")�   @   B           �   ?   A           �   >   @          3input = lambda: sys.stdin.readline().rstrip("\r\n")�   =   ?          Csys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)�   <   >           �   ;   =           �   :   <          F        self.readline = lambda: self.buffer.readline().decode("ascii")�   9   ;          >        self.read = lambda: self.buffer.read().decode("ascii")�   8   :          C        self.write = lambda s: self.buffer.write(s.encode("ascii"))�   7   9          ,        self.writable = self.buffer.writable�   6   8          &        self.flush = self.buffer.flush�   5   7          "        self.buffer = FastIO(file)�   4   6              def __init__(self, file):�   3   5          class IOWrapper(IOBase):�   2   4           �   1   3           �   0   2          8            self.buffer.truncate(0), self.buffer.seek(0)�   /   1          ;            self.os.write(self._fd, self.buffer.getvalue())�   .   0                  if self.writable:�   -   /              def flush(self):�   ,   .           �   +   -          %        return self.buffer.readline()�   *   ,                  self.newlines -= 1�   )   +          O            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)�   (   *          $            ptr = self.buffer.tell()�   '   )          4            self.newlines = b.count(b"\n") + (not b)�   &   (          U            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))�   %   '          !        while self.newlines == 0:�   $   &              def readline(self):�   #   %           �   "   $          !        return self.buffer.read()�   !   #                  self.newlines = 0�       "          O            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)�      !          $            ptr = self.buffer.tell()�                                 break�                            if not b:�                U            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))�                        while True:�                    def read(self):�                 �                A        self.write = self.buffer.write if self.writable else None�                @        self.writable = "x" in file.mode or "r" not in file.mode�                        self.buffer = BytesIO()�                         self._fd = file.fileno()�                        self.os = os�                 �                        import os�                    def __init__(self, file):�                 �                    newlines = 0�                class FastIO(IOBase):�                 �                 �                sys.setrecursionlimit(10 ** 5)�   
             BUFSIZE = 8192�   	              �      
           from itertools import accumulate�      	          from operator import add�                from heapq import *�                import math, string�                3from collections import defaultdict, deque, Counter�                from bisect import *�                from types import GeneratorType�                from io import BytesIO, IOBase�                 import os, sys5��                                                �                                              �                         .                     �                         N                     �               3       3   c       3       3       �                         �                     �                         �                     �                         �                     �                           �                       �    	                       �                       �    
                     �                     �                         	                    �                           (                      �                           )                      �                         *                    �                         @                    �                           Q                      �                         R                    �                         p                    �                           �                      �                         �                    �                           �                      �                         �                    �               @       @   �      @       @       �               A       A         A       A       �                           \                      �                         ]                    �                         q                    �               U       U   �      U       U       �                         �                    �                         �                    �               $       $         $       $       �                O       O   ,      O       O       �    !                     |                    �    "           !       !   �      !       !       �    #                       �                      �    $                     �                    �    %           !       !   �      !       !       �    &           U       U   �      U       U       �    '           4       4   I      4       4       �    (           $       $   ~      $       $       �    )           O       O   �      O       O       �    *                     �                    �    +           %       %         %       %       �    ,                       4                      �    -                     5                    �    .                     J                    �    /           ;       ;   d      ;       ;       �    0           8       8   �      8       8       �    1                       �                      �    2                       �                      �    3                     �                    �    4                     �                    �    5           "       "         "       "       �    6           &       &   5      &       &       �    7           ,       ,   \      ,       ,       �    8           C       C   �      C       C       �    9           >       >   �      >       >       �    :           F       F         F       F       �    ;                       S                      �    <                       T                      �    =           C       C   U      C       C       �    >           3       3   �      3       3       �    ?                       �                      �    @                       �                      �    A                     �                    �    B           !       !   �      !       !       �    C           %       %         %       %       �    D                       *                      �    E                       +                      �    F                     ,                    �    G           %       %   F      %       %       �    H                     l                    �    I                       �                      �    J                       �                      �    K                     �                    �    L                       �                      �    M                     �                    �    N           
       
   �      
       
       �    O                       �                      �    P                      �                     �    Q                     �                    �    R                     �                    �    S                      �                     �    T                      �                     �    U                     �                    �    V                     �                    �    W                      	                     �    X                      	                     �    Y                     	                    �    Z                     +	                    �    [                     H	                    �    \                     ]	                    �    ]                     k	                    �    ^                      �	                     �    _           	           �	      	               �    `                   	   �	              	       �    a                      �	                     �    b                     �	                    �    c                   !   �	              !       �    d                      �	                     �    e                     �	                    �    f                     �	                    �    g                      �	                     �    h           !           
      !               �    i                   !   
              !       �    j                      &
                     �    k                      '
                     �    l                      (
              !       5��