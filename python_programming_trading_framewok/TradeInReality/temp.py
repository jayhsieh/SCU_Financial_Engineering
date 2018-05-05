
'
'
'


C
r
e
a
t
e
d
 
o
n
 
2
0
1
8
年
4
月
3
0
日




@
a
u
t
h
o
r
:
 
A
l
b
e
r
t


'
'
'


f
r
o
m
 
R
e
a
l
T
i
m
e
.
f
u
n
c
t
i
o
n
 
i
m
p
o
r
t
 
g
e
t
M
a
t
c
h
,
 
g
e
t
O
r
d
e
r


i
m
p
o
r
t
 
d
a
t
e
t
i
m
e


f
r
o
m
 
R
e
a
l
T
i
m
e
.
o
r
d
e
r
 
i
m
p
o
r
t
 
O
r
d
e
r
M
K
T








#
取
得
報
價
資
訊
，
詳
情
請
查
看
技
巧
5
1


w
i
t
h
 
o
p
e
n
(
'
f
u
n
c
t
i
o
n
.
p
y
'
,
'
r
'
)
 
a
s
 
f
:


	
e
x
e
c
(
f
.
r
e
a
d
(
)
)


#
取
得
下
單
函
數
，
詳
情
請
查
看
技
巧
1
0
3


w
i
t
h
 
o
p
e
n
(
'
o
r
d
e
r
.
p
y
'
,
'
r
'
)
 
a
s
 
f
:


	
e
x
e
c
(
f
.
r
e
a
d
(
)
)




#
定
義
趨
勢
判
斷
時
間


t
r
e
n
d
T
i
m
e
1
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
'
0
8
:
5
0
:
0
0
.
0
0
'
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


t
r
e
n
d
T
i
m
e
2
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
'
0
9
:
0
0
:
0
0
.
0
0
'
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


t
r
e
n
d
T
i
m
e
3
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
'
0
9
:
0
3
:
0
0
.
0
0
'
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


t
r
e
n
d
N
u
m
=
0


t
r
e
n
d
=
0




#
設
定
指
標
變
數


M
A
a
r
r
a
y
=
[
]


M
A
n
u
m
=
1
0


l
a
s
t
H
M
T
i
m
e
=
"
"


l
a
s
t
M
A
V
a
l
u
e
=
0


l
a
s
t
P
r
i
c
e
=
0




#
設
定
初
始
倉
位
，
若
為
0
則
為
無
在
倉
部
位


i
n
d
e
x
=
0


o
r
d
e
r
T
i
m
e
=
0


o
r
d
e
r
P
r
i
c
e
=
0


c
o
v
e
r
T
i
m
e
=
0


c
o
v
e
r
P
r
i
c
e
=
0




#
判
斷
趨
勢


f
o
r
 
i
 
i
n
 
g
e
t
O
r
d
e
r
(
)
:
 
 
 
 


	
O
r
d
e
r
I
n
f
o
=
i
.
s
p
l
i
t
(
'
,
'
)


	
O
r
d
e
r
T
i
m
e
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
O
r
d
e
r
I
n
f
o
[
0
]
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


	
O
r
d
e
r
B
C
n
t
=
i
n
t
(
O
r
d
e
r
I
n
f
o
[
1
]
)


	
O
r
d
e
r
B
A
m
o
u
n
t
=
f
l
o
a
t
(
O
r
d
e
r
I
n
f
o
[
2
]
)


	
O
r
d
e
r
S
C
n
t
=
i
n
t
(
O
r
d
e
r
I
n
f
o
[
3
]
)


	
O
r
d
e
r
S
A
m
o
u
n
t
=
f
l
o
a
t
(
O
r
d
e
r
I
n
f
o
[
4
]
)




	
#
趨
勢
判
斷
1


	
i
f
 
O
r
d
e
r
T
i
m
e
>
=
t
r
e
n
d
T
i
m
e
1
 
a
n
d
 
t
r
e
n
d
N
u
m
=
=
0
:


	
	
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
>
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:


	
	
	
t
r
e
n
d
+
=
1


	
	
e
l
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
<
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:
 
 
 


	
	
	
t
r
e
n
d
-
=
1
 


	
	
t
r
e
n
d
N
u
m
+
=
1


	
	
p
r
i
n
t
(
 
O
r
d
e
r
I
n
f
o
[
0
]
,
"
B
"
,
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
,
"
S
"
,
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
)




	
#
趨
勢
判
斷
2


	
i
f
 
O
r
d
e
r
T
i
m
e
>
=
t
r
e
n
d
T
i
m
e
2
 
a
n
d
 
t
r
e
n
d
N
u
m
=
=
1
:


	
	
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
>
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:


	
	
	
t
r
e
n
d
+
=
1


	
	
e
l
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
<
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:
 
 
 


	
	
	
t
r
e
n
d
-
=
1


	
	
t
r
e
n
d
N
u
m
+
=
1


	
	
p
r
i
n
t
(
 
O
r
d
e
r
I
n
f
o
[
0
]
,
"
B
"
,
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
,
"
S
"
,
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
)




	
#
趨
勢
判
斷
3


	
i
f
 
O
r
d
e
r
T
i
m
e
>
=
t
r
e
n
d
T
i
m
e
3
 
a
n
d
 
t
r
e
n
d
N
u
m
=
=
2
:


	
	
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
>
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:


	
	
	
t
r
e
n
d
+
=
1


	
	
e
l
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
<
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:
 
 
 


	
	
	
t
r
e
n
d
-
=
1


	
	
p
r
i
n
t
(
 
O
r
d
e
r
I
n
f
o
[
0
]
,
"
B
"
,
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
,
"
S
"
,
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
)


	
	
b
r
e
a
k
 






#
進
場
判
斷


f
o
r
 
i
 
i
n
 
g
e
t
M
a
t
c
h
(
)
:
	
	


	
M
a
t
c
h
I
n
f
o
=
i
.
s
p
l
i
t
(
'
,
'
)


	
H
M
T
i
m
e
=
M
a
t
c
h
I
n
f
o
[
0
]
[
0
:
2
]
+
M
a
t
c
h
I
n
f
o
[
0
]
[
3
:
5
]


	
M
a
t
c
h
P
r
i
c
e
=
i
n
t
(
M
a
t
c
h
I
n
f
o
[
1
]
)




	
#
計
算
M
A


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
0
:


	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e


	
e
l
s
e
:


	
	
i
f
 
H
M
T
i
m
e
=
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
M
A
a
r
r
a
y
[
-
1
]
=
M
a
t
c
h
P
r
i
c
e


	
	
e
l
i
f
 
H
M
T
i
m
e
!
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
<
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
e
l
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
=
M
A
a
r
r
a
y
[
1
:
]
+
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e




	
#
當
M
A
計
算
完
成
後
，
開
始
判
斷
進
場


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
 
:


	
	
M
A
V
a
l
u
e
=
f
l
o
a
t
(
s
u
m
(
M
A
a
r
r
a
y
)
)
/
l
e
n
(
M
A
a
r
r
a
y
)


	
	
i
f
 
l
a
s
t
M
A
V
a
l
u
e
=
=
0
 
a
n
d
 
l
a
s
t
P
r
i
c
e
=
=
0
:


	
	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e


	
	
	
c
o
n
t
i
n
u
e


	
	
p
r
i
n
t
(
 
"
P
r
i
c
e
"
,
M
a
t
c
h
P
r
i
c
e
,
"
M
A
"
,
M
A
V
a
l
u
e
 
)


	
	
#
多
方
進
場
判
斷


	
	
i
f
 
t
r
e
n
d
>
=
1
:


	
	
	
#
當
價
格
向
上
突
破
M
A


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
>
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
<
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
1


	
	
	
	
o
r
d
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
B
'
,
'
1
'
)


	
	
	
	
o
r
d
e
r
T
i
m
e
=
o
r
d
e
r
I
n
f
o
[
6
]


	
	
	
	
o
r
d
e
r
P
r
i
c
e
=
i
n
t
(
o
r
d
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
o
r
d
e
r
T
i
m
e
,
"
O
r
d
e
r
 
B
u
y
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
o
r
d
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
#
空
方
進
場
判
斷
 
 


	
	
e
l
i
f
 
t
r
e
n
d
<
=
-
1
:


	
	
	
#
當
價
格
向
下
突
破
M
A


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
<
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
>
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
1


	
	
	
	
o
r
d
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
S
'
,
'
1
'
)


	
	
	
	
o
r
d
e
r
T
i
m
e
=
o
r
d
e
r
I
n
f
o
[
6
]


	
	
	
	
o
r
d
e
r
P
r
i
c
e
=
i
n
t
(
o
r
d
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
o
r
d
e
r
T
i
m
e
,
"
O
r
d
e
r
 
S
e
l
l
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
o
r
d
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e
 




#
出
場
判
斷


f
o
r
 
i
 
i
n
 
g
e
t
M
a
t
c
h
(
)
:
 
 
 
 


	
M
a
t
c
h
I
n
f
o
=
i
.
s
p
l
i
t
(
'
,
'
)


	
H
M
T
i
m
e
=
M
a
t
c
h
I
n
f
o
[
0
]
[
0
:
2
]
+
M
a
t
c
h
I
n
f
o
[
0
]
[
3
:
5
]


	
M
a
t
c
h
P
r
i
c
e
=
i
n
t
(
M
a
t
c
h
I
n
f
o
[
1
]
)




	
#
計
算
M
A


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
0
:


	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e


	
e
l
s
e
:


	
	
i
f
 
H
M
T
i
m
e
=
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
M
A
a
r
r
a
y
[
-
1
]
=
M
a
t
c
h
P
r
i
c
e


	
	
e
l
i
f
 
H
M
T
i
m
e
!
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
<
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
e
l
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
=
M
A
a
r
r
a
y
[
1
:
]
+
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e




	
#
M
A
計
算
後
出
場
判
斷


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
 
:


	
	
M
A
V
a
l
u
e
=
f
l
o
a
t
(
s
u
m
(
M
A
a
r
r
a
y
)
)
/
l
e
n
(
M
A
a
r
r
a
y
)


	
	
i
f
 
l
a
s
t
M
A
V
a
l
u
e
=
=
0
 
a
n
d
 
l
a
s
t
P
r
i
c
e
=
=
0
:


	
	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e


	
	
	
c
o
n
t
i
n
u
e


	
	
p
r
i
n
t
(
 
"
P
r
i
c
e
"
,
M
a
t
c
h
P
r
i
c
e
,
"
M
A
"
,
M
A
V
a
l
u
e
 
)


	
	
#
當
價
格
向
下
穿
越
M
A
則
出
場


	
	
i
f
 
i
n
d
e
x
=
=
1
:


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
<
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
>
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
0


	
	
	
	
c
o
v
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
S
'
,
'
1
'
)


	
	
	
	
c
o
v
e
r
T
i
m
e
=
c
o
v
e
r
I
n
f
o
[
6
]


	
	
	
	
c
o
v
e
r
P
r
i
c
e
=
i
n
t
(
c
o
v
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
c
o
v
e
r
T
i
m
e
,
"
O
r
d
e
r
 
S
e
l
l
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
c
o
v
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
#
當
價
格
向
上
穿
越
M
A
則
出
場


	
	
e
l
i
f
 
i
n
d
e
x
=
=
-
1
:


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
>
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
<
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
0


	
	
	
	
c
o
v
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
B
'
,
'
1
'
)


	
	
	
	
c
o
v
e
r
T
i
m
e
=
c
o
v
e
r
I
n
f
o
[
6
]


	
	
	
	
c
o
v
e
r
P
r
i
c
e
=
i
n
t
(
c
o
v
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
c
o
v
e
r
T
i
m
e
,
"
O
r
d
e
r
 
B
u
y
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
c
o
v
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e
 





'
'
'


C
r
e
a
t
e
d
 
o
n
 
2
0
1
8
年
4
月
3
0
日




@
a
u
t
h
o
r
:
 
A
l
b
e
r
t


'
'
'


f
r
o
m
 
R
e
a
l
T
i
m
e
.
f
u
n
c
t
i
o
n
 
i
m
p
o
r
t
 
g
e
t
M
a
t
c
h
,
 
g
e
t
O
r
d
e
r


i
m
p
o
r
t
 
d
a
t
e
t
i
m
e


f
r
o
m
 
R
e
a
l
T
i
m
e
.
o
r
d
e
r
 
i
m
p
o
r
t
 
O
r
d
e
r
M
K
T








#
取
得
報
價
資
訊
，
詳
情
請
查
看
技
巧
5
1


w
i
t
h
 
o
p
e
n
(
'
f
u
n
c
t
i
o
n
.
p
y
'
,
'
r
'
)
 
a
s
 
f
:


	
e
x
e
c
(
f
.
r
e
a
d
(
)
)


#
取
得
下
單
函
數
，
詳
情
請
查
看
技
巧
1
0
3


w
i
t
h
 
o
p
e
n
(
'
o
r
d
e
r
.
p
y
'
,
'
r
'
)
 
a
s
 
f
:


	
e
x
e
c
(
f
.
r
e
a
d
(
)
)




#
定
義
趨
勢
判
斷
時
間


t
r
e
n
d
T
i
m
e
1
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
'
0
8
:
5
0
:
0
0
.
0
0
'
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


t
r
e
n
d
T
i
m
e
2
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
'
0
9
:
0
0
:
0
0
.
0
0
'
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


t
r
e
n
d
T
i
m
e
3
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
'
0
9
:
0
3
:
0
0
.
0
0
'
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


t
r
e
n
d
N
u
m
=
0


t
r
e
n
d
=
0




#
設
定
指
標
變
數


M
A
a
r
r
a
y
=
[
]


M
A
n
u
m
=
1
0


l
a
s
t
H
M
T
i
m
e
=
"
"


l
a
s
t
M
A
V
a
l
u
e
=
0


l
a
s
t
P
r
i
c
e
=
0




#
設
定
初
始
倉
位
，
若
為
0
則
為
無
在
倉
部
位


i
n
d
e
x
=
0


o
r
d
e
r
T
i
m
e
=
0


o
r
d
e
r
P
r
i
c
e
=
0


c
o
v
e
r
T
i
m
e
=
0


c
o
v
e
r
P
r
i
c
e
=
0




#
判
斷
趨
勢


f
o
r
 
i
 
i
n
 
g
e
t
O
r
d
e
r
(
)
:
 
 
 
 


	
O
r
d
e
r
I
n
f
o
=
i
.
s
p
l
i
t
(
'
,
'
)


	
O
r
d
e
r
T
i
m
e
=
d
a
t
e
t
i
m
e
.
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
O
r
d
e
r
I
n
f
o
[
0
]
,
"
%
H
:
%
M
:
%
S
.
%
f
"
)


	
O
r
d
e
r
B
C
n
t
=
i
n
t
(
O
r
d
e
r
I
n
f
o
[
1
]
)


	
O
r
d
e
r
B
A
m
o
u
n
t
=
f
l
o
a
t
(
O
r
d
e
r
I
n
f
o
[
2
]
)


	
O
r
d
e
r
S
C
n
t
=
i
n
t
(
O
r
d
e
r
I
n
f
o
[
3
]
)


	
O
r
d
e
r
S
A
m
o
u
n
t
=
f
l
o
a
t
(
O
r
d
e
r
I
n
f
o
[
4
]
)




	
#
趨
勢
判
斷
1


	
i
f
 
O
r
d
e
r
T
i
m
e
>
=
t
r
e
n
d
T
i
m
e
1
 
a
n
d
 
t
r
e
n
d
N
u
m
=
=
0
:


	
	
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
>
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:


	
	
	
t
r
e
n
d
+
=
1


	
	
e
l
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
<
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:
 
 
 


	
	
	
t
r
e
n
d
-
=
1
 


	
	
t
r
e
n
d
N
u
m
+
=
1


	
	
p
r
i
n
t
(
 
O
r
d
e
r
I
n
f
o
[
0
]
,
"
B
"
,
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
,
"
S
"
,
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
)




	
#
趨
勢
判
斷
2


	
i
f
 
O
r
d
e
r
T
i
m
e
>
=
t
r
e
n
d
T
i
m
e
2
 
a
n
d
 
t
r
e
n
d
N
u
m
=
=
1
:


	
	
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
>
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:


	
	
	
t
r
e
n
d
+
=
1


	
	
e
l
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
<
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:
 
 
 


	
	
	
t
r
e
n
d
-
=
1


	
	
t
r
e
n
d
N
u
m
+
=
1


	
	
p
r
i
n
t
(
 
O
r
d
e
r
I
n
f
o
[
0
]
,
"
B
"
,
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
,
"
S
"
,
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
)




	
#
趨
勢
判
斷
3


	
i
f
 
O
r
d
e
r
T
i
m
e
>
=
t
r
e
n
d
T
i
m
e
3
 
a
n
d
 
t
r
e
n
d
N
u
m
=
=
2
:


	
	
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
>
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:


	
	
	
t
r
e
n
d
+
=
1


	
	
e
l
i
f
 
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
 
<
 
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
:
 
 
 


	
	
	
t
r
e
n
d
-
=
1


	
	
p
r
i
n
t
(
 
O
r
d
e
r
I
n
f
o
[
0
]
,
"
B
"
,
O
r
d
e
r
B
A
m
o
u
n
t
/
O
r
d
e
r
B
C
n
t
,
"
S
"
,
O
r
d
e
r
S
A
m
o
u
n
t
/
O
r
d
e
r
S
C
n
t
)


	
	
b
r
e
a
k
 






#
進
場
判
斷


f
o
r
 
i
 
i
n
 
g
e
t
M
a
t
c
h
(
)
:
	
	


	
M
a
t
c
h
I
n
f
o
=
i
.
s
p
l
i
t
(
'
,
'
)


	
H
M
T
i
m
e
=
M
a
t
c
h
I
n
f
o
[
0
]
[
0
:
2
]
+
M
a
t
c
h
I
n
f
o
[
0
]
[
3
:
5
]


	
M
a
t
c
h
P
r
i
c
e
=
i
n
t
(
M
a
t
c
h
I
n
f
o
[
1
]
)




	
#
計
算
M
A


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
0
:


	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e


	
e
l
s
e
:


	
	
i
f
 
H
M
T
i
m
e
=
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
M
A
a
r
r
a
y
[
-
1
]
=
M
a
t
c
h
P
r
i
c
e


	
	
e
l
i
f
 
H
M
T
i
m
e
!
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
<
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
e
l
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
=
M
A
a
r
r
a
y
[
1
:
]
+
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e




	
#
當
M
A
計
算
完
成
後
，
開
始
判
斷
進
場


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
 
:


	
	
M
A
V
a
l
u
e
=
f
l
o
a
t
(
s
u
m
(
M
A
a
r
r
a
y
)
)
/
l
e
n
(
M
A
a
r
r
a
y
)


	
	
i
f
 
l
a
s
t
M
A
V
a
l
u
e
=
=
0
 
a
n
d
 
l
a
s
t
P
r
i
c
e
=
=
0
:


	
	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e


	
	
	
c
o
n
t
i
n
u
e


	
	
p
r
i
n
t
(
 
"
P
r
i
c
e
"
,
M
a
t
c
h
P
r
i
c
e
,
"
M
A
"
,
M
A
V
a
l
u
e
 
)


	
	
#
多
方
進
場
判
斷


	
	
i
f
 
t
r
e
n
d
>
=
1
:


	
	
	
#
當
價
格
向
上
突
破
M
A


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
>
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
<
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
1


	
	
	
	
o
r
d
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
B
'
,
'
1
'
)


	
	
	
	
o
r
d
e
r
T
i
m
e
=
o
r
d
e
r
I
n
f
o
[
6
]


	
	
	
	
o
r
d
e
r
P
r
i
c
e
=
i
n
t
(
o
r
d
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
o
r
d
e
r
T
i
m
e
,
"
O
r
d
e
r
 
B
u
y
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
o
r
d
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
#
空
方
進
場
判
斷
 
 


	
	
e
l
i
f
 
t
r
e
n
d
<
=
-
1
:


	
	
	
#
當
價
格
向
下
突
破
M
A


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
<
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
>
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
1


	
	
	
	
o
r
d
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
S
'
,
'
1
'
)


	
	
	
	
o
r
d
e
r
T
i
m
e
=
o
r
d
e
r
I
n
f
o
[
6
]


	
	
	
	
o
r
d
e
r
P
r
i
c
e
=
i
n
t
(
o
r
d
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
o
r
d
e
r
T
i
m
e
,
"
O
r
d
e
r
 
S
e
l
l
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
o
r
d
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e
 




#
出
場
判
斷


f
o
r
 
i
 
i
n
 
g
e
t
M
a
t
c
h
(
)
:
 
 
 
 


	
M
a
t
c
h
I
n
f
o
=
i
.
s
p
l
i
t
(
'
,
'
)


	
H
M
T
i
m
e
=
M
a
t
c
h
I
n
f
o
[
0
]
[
0
:
2
]
+
M
a
t
c
h
I
n
f
o
[
0
]
[
3
:
5
]


	
M
a
t
c
h
P
r
i
c
e
=
i
n
t
(
M
a
t
c
h
I
n
f
o
[
1
]
)




	
#
計
算
M
A


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
0
:


	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e


	
e
l
s
e
:


	
	
i
f
 
H
M
T
i
m
e
=
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
M
A
a
r
r
a
y
[
-
1
]
=
M
a
t
c
h
P
r
i
c
e


	
	
e
l
i
f
 
H
M
T
i
m
e
!
=
l
a
s
t
H
M
T
i
m
e
:


	
	
	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
<
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
+
=
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
e
l
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
:


	
	
	
	
M
A
a
r
r
a
y
=
M
A
a
r
r
a
y
[
1
:
]
+
[
M
a
t
c
h
P
r
i
c
e
]


	
	
	
l
a
s
t
H
M
T
i
m
e
=
H
M
T
i
m
e




	
#
M
A
計
算
後
出
場
判
斷


	
i
f
 
l
e
n
(
M
A
a
r
r
a
y
)
=
=
M
A
n
u
m
 
:


	
	
M
A
V
a
l
u
e
=
f
l
o
a
t
(
s
u
m
(
M
A
a
r
r
a
y
)
)
/
l
e
n
(
M
A
a
r
r
a
y
)


	
	
i
f
 
l
a
s
t
M
A
V
a
l
u
e
=
=
0
 
a
n
d
 
l
a
s
t
P
r
i
c
e
=
=
0
:


	
	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e


	
	
	
c
o
n
t
i
n
u
e


	
	
p
r
i
n
t
(
 
"
P
r
i
c
e
"
,
M
a
t
c
h
P
r
i
c
e
,
"
M
A
"
,
M
A
V
a
l
u
e
 
)


	
	
#
當
價
格
向
下
穿
越
M
A
則
出
場


	
	
i
f
 
i
n
d
e
x
=
=
1
:


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
<
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
>
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
0


	
	
	
	
c
o
v
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
S
'
,
'
1
'
)


	
	
	
	
c
o
v
e
r
T
i
m
e
=
c
o
v
e
r
I
n
f
o
[
6
]


	
	
	
	
c
o
v
e
r
P
r
i
c
e
=
i
n
t
(
c
o
v
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
c
o
v
e
r
T
i
m
e
,
"
O
r
d
e
r
 
S
e
l
l
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
c
o
v
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
#
當
價
格
向
上
穿
越
M
A
則
出
場


	
	
e
l
i
f
 
i
n
d
e
x
=
=
-
1
:


	
	
	
i
f
 
M
a
t
c
h
P
r
i
c
e
>
M
A
V
a
l
u
e
 
a
n
d
 
l
a
s
t
P
r
i
c
e
<
=
l
a
s
t
M
A
V
a
l
u
e
:


	
	
	
	
i
n
d
e
x
=
0


	
	
	
	
c
o
v
e
r
I
n
f
o
=
O
r
d
e
r
M
K
T
(
'
T
X
0
0
'
,
'
B
'
,
'
1
'
)


	
	
	
	
c
o
v
e
r
T
i
m
e
=
c
o
v
e
r
I
n
f
o
[
6
]


	
	
	
	
c
o
v
e
r
P
r
i
c
e
=
i
n
t
(
c
o
v
e
r
I
n
f
o
[
4
]
)


	
	
	
	
p
r
i
n
t
(
 
c
o
v
e
r
T
i
m
e
,
"
O
r
d
e
r
 
B
u
y
 
S
u
c
c
e
s
s
!
 
P
r
i
c
e
:
"
,
c
o
v
e
r
P
r
i
c
e
)


	
	
	
	
b
r
e
a
k


	
	
l
a
s
t
M
A
V
a
l
u
e
=
M
A
V
a
l
u
e


	
	
l
a
s
t
P
r
i
c
e
=
M
a
t
c
h
P
r
i
c
e
 




