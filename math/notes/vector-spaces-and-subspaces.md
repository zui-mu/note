# 向量空间与矩阵的四个基本子空间

## 课程主线与当前范围

这部分课程始终围绕同一个线性方程展开：

```math
A\mathbf{x}=\mathbf{b},
\qquad
A:\mathbb{R}^n\longrightarrow\mathbb{R}^m.
```

其中 $`\mathbf{x}`$ 是输入，$`A\mathbf{x}`$ 是输出，$`\mathbf{b}`$ 是希望得到的目标输出。

| 所在一侧 | 基本子空间 | 描述的内容 |
| --- | --- | --- |
| 输出端 $`\mathbb{R}^m`$ | 列空间 $`\mathrm{Col}(A)`$ | $`A`$ 能产生哪些输出 |
| 输出端 $`\mathbb{R}^m`$ | 左零空间 $`N(A^T)`$ | 哪些方向与 $`A`$ 的全部列正交 |
| 输入端 $`\mathbb{R}^n`$ | 行空间 $`\mathrm{Col}(A^T)`$ | $`A`$ 的全部行能够张成哪些方向 |
| 输入端 $`\mathbb{R}^n`$ | 零空间 $`N(A)`$ | 哪些输入会被 $`A`$ 变成零向量 |

后文先建立子空间与张成，再从矩阵的列进入列空间；其间把矩阵和函数本身也视为向量，讨论矩阵子空间的交与和，以及线性微分方程的解空间。接着用消元识别主元、自由变量和秩，由此得到零空间。转置把同样的结构带到行空间与左零空间，四个空间最终共同说明矩阵保留、产生和消去的方向，并帮助描述 $`A\mathbf{x}=\mathbf{b}`$ 的全部解。

## 一、向量空间与子空间

### 1. $`\mathbb{R}^n`$ 的含义

```math
\mathbb{R}^n
= \{(x_1,x_2,\ldots,x_n)\mid x_1,x_2,\ldots,x_n\in\mathbb{R}\}
```

$`\mathbb{R}^n`$ 表示所有由 $`n`$ 个实数组成的向量。比如，$`\mathbb{R}^2`$ 是所有二维实向量的集合，$`\mathbb{R}^3`$ 是所有三维实向量的集合。

### 2. 向量空间中的元素与运算

抽象线性代数中的“向量”不一定是列状数字，也可以是矩阵、函数或多项式。只要一个集合配备了合适的向量加法和标量数乘，并满足向量空间的规则，其中的元素都可以称为向量。

因此，说明一个向量空间时需要明确四件事：**元素是什么、标量来自哪里、加法怎样定义、数乘怎样定义。** 对实向量空间 $`V`$，除了对加法和数乘封闭外，还要满足：

| 规则 | 数学表达 |
| --- | --- |
| 加法交换律 | $`\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}`$ |
| 加法结合律 | $`(\mathbf{u}+\mathbf{v})+\mathbf{w}=\mathbf{u}+(\mathbf{v}+\mathbf{w})`$ |
| 存在零向量 | $`\mathbf{u}+\mathbf{0}_V=\mathbf{u}`$ |
| 存在加法逆元 | $`\mathbf{u}+(-\mathbf{u})=\mathbf{0}_V`$ |
| 数乘的两种分配律 | $`a(\mathbf{u}+\mathbf{v})=a\mathbf{u}+a\mathbf{v}`$，$`(a+b)\mathbf{u}=a\mathbf{u}+b\mathbf{u}`$ |
| 数乘结合律与单位元 | $`a(b\mathbf{u})=(ab)\mathbf{u}`$，$`1\mathbf{u}=\mathbf{u}`$ |

不同教材可能把封闭性写在运算定义中，也可能把它与其他公理并列；关键是理解这些要求，而不是死记公理被数成几条。

固定大小的所有实矩阵在通常的矩阵加法与标量数乘下，也构成向量空间。此时零向量是零矩阵；在多项式空间中，零向量则是零多项式。**零向量的具体外形由空间中的元素决定。**

当矩阵本身被视为向量时，$`A+B`$ 是向量加法，$`cA`$ 是标量数乘，而 $`AB`$ 是矩阵之间的乘法。向量空间的定义不要求对 $`AB`$ 封闭，因此判断矩阵集合是否为子空间时，不需要检查矩阵乘法。

> **变化的是元素的外形，不变的是线性组合、线性无关、基和维数这些概念。**

### 3. 子空间与封闭性

子空间是原向量空间中的一个子集，沿用原空间的标量域、加法与数乘，并且它自己也构成向量空间。判断**非空集合** $`S`$ 是否为子空间，可以检查：对任意 $`\mathbf{u},\mathbf{v}\in S`$ 和任意实数 $`a,b`$，是否都有

```math
a\mathbf{u}+b\mathbf{v}\in S.
```

这叫作对线性组合封闭。它同时包含两个基本要求：

```math
\mathbf{u}+\mathbf{v}\in S,
\qquad
c\mathbf{u}\in S.
```

令 $`a=b=0`$，还可以得到零向量，因此**子空间一定包含零向量**。

非空条件不能省略，否则空集会形式上满足“对已有元素的线性组合封闭”，却不包含零向量。等价地，也可以分别检查零向量、加法封闭和数乘封闭；交换律、结合律与分配律等规则已经从环境空间继承下来。

例如，$`x`$ 轴

```math
S=\{(x,0)\mid x\in\mathbb{R}\}
```

满足

```math
a(x_1,0)+b(x_2,0)=(ax_1+bx_2,0)\in S,
```

所以它是 $`\mathbb{R}^2`$ 的子空间。

水平直线

```math
T=\{(x,1)\mid x\in\mathbb{R}\}
```

不是子空间，因为它不包含 $`(0,0)`$，并且

```math
(2,1)+(5,1)=(7,2)\notin T.
```

向量空间 $`V`$ 本身和零空间 $`\{\mathbf{0}_V\}`$ 都是 $`V`$ 的子空间。若有限维空间中的子空间 $`S\subseteq V`$ 满足 $`\dim S=\dim V`$，则 $`S=V`$；只有真子空间的维数才严格更小。

### 4. 张成

给定向量 $`\mathbf{v}_1,\ldots,\mathbf{v}_k`$，选定一组具体系数后得到的

```math
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k
```

叫作一个**线性组合**（linear combination）。让所有系数在实数范围内任意变化，所得全部线性组合构成的集合叫作这些向量的**张成**（span）：

```math
\mathrm{span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}
= \{c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k
\mid c_1,\ldots,c_k\in\mathbb{R}\}.
```

因此，linear combination 指某一个具体结果，span 指把所有可能的系数都取一遍后得到的整个集合。例如，

```math
\mathrm{span}\left\{
\begin{bmatrix}1\\2\end{bmatrix}
\right\}
=\left\{
c\begin{bmatrix}1\\2\end{bmatrix}
\mid c\in\mathbb{R}
\right\}
```

是一条经过原点的直线；而

```math
\mathrm{span}\left\{
\begin{bmatrix}1\\0\end{bmatrix},
\begin{bmatrix}0\\1\end{bmatrix}
\right\}
=\mathbb{R}^2.
```

张成集合包含零向量，并且对加法和数乘封闭，所以它一定是子空间。它还是包含 $`\mathbf{v}_1,\ldots,\mathbf{v}_k`$ 的**最小子空间**：任何包含这些向量的子空间，也必须包含它们的一切线性组合。几何上，张成可能是原点、过原点的直线、过原点的平面，或者更高维的子空间；它也可以等于整个环境空间。

> **张成关注的是所有线性组合：这些向量通过任意数乘与相加，最终能够覆盖出整个什么空间。**

子空间与张成为后面两个核心对象提供了共同语言：

**列空间是矩阵各列的张成，零空间是齐次方程全部解组成的子空间。**

## 二、从矩阵方程到列空间

### 1. $`A\mathbf{x}=\mathbf{b}`$ 的尺寸

若

```math
A\in\mathbb{R}^{m\times n},
```

那么

```math
\underbrace{A}_{m\times n}
\underbrace{\mathbf{x}}_{n\times1}
= \underbrace{\mathbf{b}}_{m\times1}.
```

矩阵结构与方程组的对应关系是：

| 矩阵结构 | 方程组含义 |
| --- | --- |
| $`m`$ 行 | $`m`$ 个方程 |
| $`n`$ 列 | $`n`$ 个未知数 |
| 第 $`i`$ 行 | 第 $`i`$ 个方程的系数 |
| 第 $`j`$ 列 | 未知数 $`x_j`$ 在全部方程中的系数 |

同一个矩阵可以从三个角度理解：

1. 按行看，它是一组方程。
2. 按列看，$`A\mathbf{x}`$ 是矩阵各列的线性组合。
3. 看成线性变换，它把 $`\mathbb{R}^n`$ 中的输入送到 $`\mathbb{R}^m`$ 中：

```math
A:\mathbb{R}^n\longrightarrow\mathbb{R}^m.
```

### 2. 矩阵乘向量的列视角

把矩阵写成列向量形式：

```math
A=
\begin{bmatrix}
\mathbf{a}_1&\mathbf{a}_2&\cdots&\mathbf{a}_n
\end{bmatrix}.
```

那么

```math
A\mathbf{x}
= x_1\mathbf{a}_1+x_2\mathbf{a}_2+\cdots+x_n\mathbf{a}_n.
```

因此，矩阵乘向量的本质是：用输入向量 $`\mathbf{x}`$ 的各个分量作为系数，对矩阵各列进行线性组合。

### 3. 列空间

矩阵各列的所有线性组合组成矩阵的**列空间**：

```math
\mathrm{Col}(A)
= \mathrm{span}\{\mathbf{a}_1,\ldots,\mathbf{a}_n\}
= \{A\mathbf{x}\mid\mathbf{x}\in\mathbb{R}^n\}.
```

每个列向量都有 $`m`$ 个分量，所以

```math
\mathrm{Col}(A)\subseteq\mathbb{R}^m.
```

列空间描述的是矩阵能够产生的全部输出，不一定等于整个 $`\mathbb{R}^m`$。

列空间确实是子空间。若 $`\mathbf{u}=A\mathbf{x}_1`$、$`\mathbf{v}=A\mathbf{x}_2`$ 都属于 $`\mathrm{Col}(A)`$，则对任意实数 $`\alpha,\beta`$，

```math
\alpha\mathbf{u}+\beta\mathbf{v}
=A(\alpha\mathbf{x}_1+\beta\mathbf{x}_2)
\in\mathrm{Col}(A).
```

它也包含 $`A\mathbf{0}=\mathbf{0}`$，所以对线性组合封闭且非空。

### 4. 右端向量与解的存在性

在 $`A\mathbf{x}=\mathbf{b}`$ 中，$`\mathbf{b}`$ 称为 **right-hand side（右端向量，RHS）**，它是希望矩阵产生的目标输出。

由于 $`A\mathbf{x}`$ 是矩阵各列的线性组合，所以

```math
A\mathbf{x}=\mathbf{b}\text{ 有解}
\quad\Longleftrightarrow\quad
\mathbf{b}\in\mathrm{Col}(A).
```

方程数与未知数数只能提供线索，不能单独决定某个具体方程组是否有解：

- 当 $`m>n`$ 时，方程较多，某些条件可能冲突，但特定的 $`\mathbf{b}`$ 仍可能有解。
- 当 $`m<n`$ 时，也可能因为方程冲突而无解；一旦有解，则一定存在自由变量，所以不会只有唯一解。

判断 $`\mathbf{b}`$ 能否到达之后，还需要确定哪些列真正扩大了列空间、哪些列只是已有方向的重复组合。

## 三、列空间中的独立方向、基与秩

### 1. 冗余列与线性相关

向量组 $`\mathbf{v}_1,\ldots,\mathbf{v}_k`$ **线性无关**（linearly independent），是指方程

```math
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k=\mathbf{0}
```

只有平凡解

```math
c_1=\cdots=c_k=0.
```

只要能找到一组不全为零的系数，仍使线性组合等于零向量，这组向量就**线性相关**（linearly dependent）。线性无关关注的不是向量能组合出多少结果，而是它们之间是否存在冗余关系。

考虑贯穿后文的矩阵

```math
A=
\begin{bmatrix}
1&2&3\\
2&4&6\\
2&6&8\\
2&8&10
\end{bmatrix}
= \begin{bmatrix}
\mathbf{a}_1&\mathbf{a}_2&\mathbf{a}_3
\end{bmatrix}.
```

它的第三列满足

```math
\mathbf{a}_3=\mathbf{a}_1+\mathbf{a}_2.
```

因此第三列没有提供新的方向：

```math
\mathrm{span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3\}
= \mathrm{span}\{\mathbf{a}_1,\mathbf{a}_2\}.
```

同时

```math
\mathbf{a}_1+\mathbf{a}_2-\mathbf{a}_3=\mathbf{0}
```

给出了一组不全为零的系数，所以三列线性相关。能够由其他列线性组合得到的列是冗余列，它可以从列空间的生成集合中去掉。

一个特别直接的判据是：**只要向量组中含有零向量，这组向量就一定线性相关。** 假设其中第 $`j`$ 个向量为 $`\mathbf{0}`$，令 $`c_j=1`$、其余系数全为 $`0`$，便得到一个系数不全为零的关系：

```math
0\mathbf{v}_1+\cdots+1\mathbf{0}+\cdots+0\mathbf{v}_k
=\mathbf{0}.
```

反过来，没有零向量并不能保证线性无关。例如，

```math
\mathbf{v}_1=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf{v}_2=\begin{bmatrix}2\\4\end{bmatrix}
=2\mathbf{v}_1
```

中的两个向量都不是零向量，但它们仍然线性相关。若矩阵的某一列是零向量，该列也不可能成为主元列，全部列组成的向量组必然线性相关。

删除冗余列会改变矩阵和未知数的数量，却不会改变能够产生的输出集合。若

```math
B=
\begin{bmatrix}
\mathbf{a}_1&\mathbf{a}_2
\end{bmatrix},
```

则 $`A\neq B`$，但

```math
\mathrm{Col}(A)=\mathrm{Col}(B).
```

所以“列空间相同”不等于“方程组相同”。

### 2. 从基到维数与秩

上一节已经得到

```math
\mathrm{Col}(A)
= \mathrm{span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3\}
= \mathrm{span}\{\mathbf{a}_1,\mathbf{a}_2\}.
```

三列都能用来生成列空间，但 $`\mathbf{a}_3`$ 可以由前两列线性组合得到，因此它是冗余的。去掉它以后，$`\mathbf{a}_1,\mathbf{a}_2`$ 仍能张成整个列空间，而且二者线性无关。

一组向量同时满足下面两个条件，就称为这个空间的一组**基**（basis）：

> “A basis for a space is a sequence of vectors $`\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_d`$ such that they are independent and they span the space.”

1. **线性无关**：只有系数全为零时，它们的线性组合才等于零向量；这保证向量组中没有冗余方向。
2. **张成整个空间**：空间中的每个向量都能由它们线性组合得到；这保证向量组没有遗漏空间中的方向。

老师把这几个概念压缩成了下面四句：

> - **Independence:** looks at combinations being zero.
> - **Spanning:** looks at all the combinations.
> - **Basis:** combines independence and spanning.
> - **Dimension:** the number of vectors in any basis, because every basis has the same number.

也就是说，线性无关排除“向量太多而产生冗余”，张成排除“向量太少而无法覆盖整个空间”。基同时满足二者，是一套**既没有冗余、又没有遗漏**的生成向量。

> **线性无关保证不多，张成保证不少；基就是刚刚好。维数则数出这份“刚刚好”中有几个向量。**

因此，本例中

```math
\{\mathbf{a}_1,\mathbf{a}_2\}
```

是 $`\mathrm{Col}(A)`$ 的一组基。基回答的是“哪些向量构成这个空间的一套独立生成方向”，所以**基是一组向量**。

接下来数这组基中有几个向量。任意一组基所含向量的个数称为空间的**维数**（dimension）。本例的基含有两个向量，所以

```math
\dim\bigl(\mathrm{Col}(A)\bigr)=2.
```

对于矩阵 $`A`$，其**秩**（rank）定义为列空间的维数，因此

```math
\mathrm{rank}(A)
= \dim\bigl(\mathrm{Col}(A)\bigr)
=2.
```

这里不能写成“基等于秩”。三者是不同类型的对象：

| 概念 | 回答的问题 | 它是什么 | 本例 |
| --- | --- | --- | --- |
| 基 | 哪些向量是独立的生成方向？ | 一组向量 | $`\{\mathbf{a}_1,\mathbf{a}_2\}`$ |
| 维数 | 这个空间有几个独立方向？ | 一个数字 | $`2`$ |
| 秩 | 矩阵的列空间有几个独立方向？ | 一个数字 | $`2`$ |

> **基属于所研究的向量空间；秩是针对矩阵而言的数字。基是一组向量；秩是矩阵列空间的一组基里有几个向量。**

研究矩阵 $`A`$ 的列空间时，二者通过“维数”联系起来：

```math
\boxed{
\text{一组基所含向量的数量}
= \dim\bigl(\mathrm{Col}(A)\bigr)
= \mathrm{rank}(A)
}
```

同一个空间可以有多组不同的基。例如，下面两组向量都能作为 $`\mathbb{R}^2`$ 的基：

```math
\left\{
\begin{bmatrix}1\\0\end{bmatrix},
\begin{bmatrix}0\\1\end{bmatrix}
\right\},
\qquad
\left\{
\begin{bmatrix}1\\1\end{bmatrix},
\begin{bmatrix}1\\-1\end{bmatrix}
\right\}.
```

它们所含的具体向量不同，但每组都有两个向量。一个空间的基可以不唯一，任意一组基所含向量的数量却一定相同，因此空间的维数是确定的。

若 $`\mathcal{B}=(\mathbf{v}_1,\ldots,\mathbf{v}_k)`$ 是一组有序基，那么空间中的每个向量 $`\mathbf{s}`$ 都能唯一写成

```math
\mathbf{s}=a_1\mathbf{v}_1+\cdots+a_k\mathbf{v}_k.
```

系数组成的列向量

```math
[\mathbf{s}]_{\mathcal{B}}
=\begin{bmatrix}a_1\\\vdots\\a_k\end{bmatrix}
```

叫作 $`\mathbf{s}`$ 在基 $`\mathcal{B}`$ 下的坐标。更换基会改变坐标，但不会改变空间的维数。零空间 $`\{\mathbf{0}\}`$ 的基是空集，维数为 $`0`$；$`\{\mathbf{0}\}`$ 本身不是它的一组基，因为含零向量的向量组线性相关。

还要区分**矩阵的尺寸**与**空间的维数**。本例中 $`A`$ 是 $`4\times3`$ 矩阵，每一列都有四个分量，因此

```math
\mathrm{Col}(A)\subseteq\mathbb{R}^4.
```

但这个列空间只有两个独立方向，所以

```math
\dim\bigl(\mathrm{Col}(A)\bigr)=2.
```

$`4\times3`$ 描述矩阵有几行几列，$`\mathbb{R}^4`$ 描述列向量所在的环境空间，而维数 $`2`$ 描述列空间自身有几个独立方向。这三个数字回答的是不同问题。

在简单矩阵中，可以直接观察哪些列是冗余的；对于一般矩阵，需要通过高斯消元找到主元列的位置。主元列的数量给出秩，而原矩阵中对应位置的列构成列空间的一组基：

```math
\boxed{
\text{主元列数量}
= \text{基向量数量}
= \dim\bigl(\mathrm{Col}(A)\bigr)
= \mathrm{rank}(A)
}
```

后文将沿着这条关系，用高斯消元系统地识别主元列、基与秩。在此之前，先把同样的基与维数概念应用到“矩阵本身作为向量”的空间。

## 四、矩阵本身构成的向量空间

### 1. 固定大小矩阵组成的空间

固定大小的所有实矩阵组成向量空间

```math
M_{m\times n}(\mathbb{R})
=\{A\mid A\text{ 是 }m\times n\text{ 实矩阵}\}.
```

这里每一个完整矩阵都是空间中的一个“向量”。向量加法和标量数乘分别是通常的矩阵加法与数乘；空间中的零向量是 $`m\times n`$ 零矩阵。

令 $`E_{ij}`$ 表示只有第 $`(i,j)`$ 个位置为 $`1`$、其余位置全为 $`0`$ 的矩阵。所有 $`E_{ij}`$ 构成 $`M_{m\times n}(\mathbb{R})`$ 的标准基，因此

```math
\dim M_{m\times n}(\mathbb{R})=mn.
```

例如，$`M_2(\mathbb{R})=M_{2\times2}(\mathbb{R})`$ 的一组标准基是

```math
E_{11}=\begin{bmatrix}1&0\\0&0\end{bmatrix},
\quad
E_{12}=\begin{bmatrix}0&1\\0&0\end{bmatrix},
\quad
E_{21}=\begin{bmatrix}0&0\\1&0\end{bmatrix},
\quad
E_{22}=\begin{bmatrix}0&0\\0&1\end{bmatrix}.
```

任意元素都能唯一写成

```math
\begin{bmatrix}a&b\\c&d\end{bmatrix}
=aE_{11}+bE_{12}+cE_{21}+dE_{22}.
```

这四个矩阵既张成整个空间又线性无关，所以

```math
\dim M_2(\mathbb{R})=4.
```

> **每个 $`2\times2`$ 矩阵是空间中的一个元素；一组标准基中有四个这样的矩阵元素。矩阵有两列，并不意味着矩阵空间是二维的。**

### 2. 与坐标向量空间的同构

选定一种固定的展开顺序，例如按行展开：

```math
\Phi\left(\begin{bmatrix}a&b\\c&d\end{bmatrix}\right)
=\begin{bmatrix}a\\b\\c\\d\end{bmatrix}.
```

这个对应是一一的，并保持线性组合：

```math
\Phi(\alpha A+\beta B)
=\alpha\Phi(A)+\beta\Phi(B).
```

因此

```math
M_2(\mathbb{R})\cong\mathbb{R}^4.
```

符号 $`\cong`$ 表示**线性同构**：两个空间的元素外形不同，但线性结构相同。它不表示矩阵集合与四维列向量集合字面上是同一个集合。只要始终使用同一种顺序，按列展开也同样可以。

### 3. 对角矩阵空间

所有 $`2\times2`$ 对角矩阵组成

```math
D_2
=\left\{
\begin{bmatrix}a&0\\0&d\end{bmatrix}
\mid a,d\in\mathbb{R}
\right\}.
```

零矩阵属于 $`D_2`$，两个对角矩阵相加后仍然对角，标量数乘后也仍然对角，所以 $`D_2`$ 是 $`M_2(\mathbb{R})`$ 的子空间。由于

```math
\begin{bmatrix}a&0\\0&d\end{bmatrix}
=aE_{11}+dE_{22},
```

$`E_{11},E_{22}`$ 张成 $`D_2`$；二者的零组合只有全零系数，所以线性无关。因此

```math
\mathcal{D}=(E_{11},E_{22})
```

是 $`D_2`$ 的一组有序基，并且

```math
\dim D_2=2.
```

例如，在这组基下，

```math
\left[
\begin{bmatrix}3&0\\0&7\end{bmatrix}
\right]_{\mathcal{D}}
=\begin{bmatrix}3\\7\end{bmatrix}.
```

这个两分量列向量是原矩阵在基 $`\mathcal{D}`$ 下的**坐标**，不是说原来的对角矩阵本身变成了 $`2\times1`$ 矩阵。

只用单位矩阵 $`I_2`$ 不能张成全部 $`D_2`$，因为

```math
cI_2=\begin{bmatrix}c&0\\0&c\end{bmatrix}
```

只能得到两个对角元素相等的矩阵。因此

```math
\mathrm{span}\{I_2\}\subsetneq D_2,
\qquad
\dim\bigl(\mathrm{span}\{I_2\}\bigr)=1.
```

另一方面，作为单个矩阵，$`I_2`$ 的两列线性无关，所以

```math
\mathrm{rank}(I_2)=2.
```

这直接揭示两个不同概念：

> **矩阵的秩描述这个矩阵的列空间有几个独立方向；矩阵张成空间的维数描述把整个矩阵当作一个元素后需要几个基元素。**

所以 $`\mathrm{rank}(I_2)=2`$，但 $`\dim(\mathrm{span}\{I_2\})=1`$，二者并不矛盾。

### 4. 对称矩阵空间

所有 $`2\times2`$ 实对称矩阵组成

```math
S_2
=\{A\in M_2(\mathbb{R})\mid A^T=A\}
=\left\{
\begin{bmatrix}a&b\\b&d\end{bmatrix}
\mid a,b,d\in\mathbb{R}
\right\}.
```

若 $`A,B\in S_2`$ 且 $`c\in\mathbb{R}`$，则

```math
\mathbf{0}^T=\mathbf{0},
\qquad
(A+B)^T=A^T+B^T=A+B,
\qquad
(cA)^T=cA^T=cA.
```

所以 $`S_2`$ 对零、加法和数乘封闭，是 $`M_2(\mathbb{R})`$ 的子空间。令

```math
F=E_{12}+E_{21}
=\begin{bmatrix}0&1\\1&0\end{bmatrix},
```

则

```math
\begin{bmatrix}a&b\\b&d\end{bmatrix}
=aE_{11}+bF+dE_{22}.
```

三个矩阵 $`E_{11},F,E_{22}`$ 张成 $`S_2`$，而零组合逐项比较会迫使三个系数全为零，所以

```math
\mathcal{S}=(E_{11},F,E_{22}),
\qquad
\dim S_2=3.
```

例如

```math
X=\begin{bmatrix}2&-1\\-1&5\end{bmatrix}
=2E_{11}-F+5E_{22},
\qquad
[X]_{\mathcal{S}}
=\begin{bmatrix}2\\-1\\5\end{bmatrix}.
```

两个非对角位置必须相等，由同一个参数控制，所以它们合起来只贡献一个独立方向。一般地，

| 矩阵空间 | 一般条件 | 一组基 | 维数 |
| --- | --- | --- | ---: |
| $`M_{m\times n}(\mathbb{R})`$ | 任意固定大小实矩阵 | 所有 $`E_{ij}`$ | $`mn`$ |
| $`D_n`$ | 非对角元素全为零 | $`E_{11},\ldots,E_{nn}`$ | $`n`$ |
| $`S_n`$ | $`A^T=A`$ | $`E_{ii}`$ 与 $`E_{ij}+E_{ji}`$，$`i<j`$ | $`n(n+1)/2`$ |

例如，$`3\times3`$ 对称矩阵有三个主对角参数和三个上三角参数，下三角由对称性决定，所以 $`\dim S_3=6`$。

自由参数的数量只有在它们给出无冗余的**线性参数化**时，才能直接读作维数。集合

```math
\{(t,t^2)\mid t\in\mathbb{R}\}
```

虽然只有一个参数，却不是线性子空间，因为 $`(1,1)`$ 在集合中，而 $`2(1,1)=(2,2)`$ 不在集合中。可靠的顺序是：**先确认子空间，再写线性参数化，最后用张成与线性无关验证基。**

对称矩阵相乘不一定仍然对称。例如

```math
A=\begin{bmatrix}1&0\\0&0\end{bmatrix},
\qquad
B=\begin{bmatrix}0&1\\1&0\end{bmatrix}
```

都对称，但

```math
AB=\begin{bmatrix}0&1\\0&0\end{bmatrix}
```

不对称。这不妨碍 $`S_2`$ 成为向量子空间，因为子空间判别检查的是矩阵加法与标量数乘，不是矩阵乘法。

### 5. 包含关系与四个基本子空间的区别

对 $`2\times2`$ 实矩阵，上面的空间满足

```math
\{\mathbf{0}\}
\subsetneq
\mathrm{span}\{I_2\}
\subsetneq
D_2
\subsetneq
S_2
\subsetneq
M_2(\mathbb{R}),
```

对应维数依次为 $`0,1,2,3,4`$。

这些**矩阵空间**与某个固定矩阵的四个基本子空间不是同一种研究对象：

- $`S_n`$ 收集所有满足对称条件的 $`n\times n`$ 矩阵，空间中的元素是一整个矩阵。
- 对固定矩阵 $`A`$，$`\mathrm{Col}(A)`$、$`N(A)`$、$`\mathrm{Col}(A^T)`$ 和 $`N(A^T)`$ 的元素是相应环境空间中的列向量。

例如，$`I_2`$ 的列空间是 $`\mathbb{R}^2`$；与此同时，$`I_2`$ 作为一个矩阵元素属于三维矩阵空间 $`S_2`$。这两句话研究的空间不同，因此并不矛盾。

### 6. 子空间的交、并与和

在 $`M_{3\times3}(\mathbb{R})`$ 中，令

```math
S=
\left\{
\begin{bmatrix}
a&b&c\\
b&d&e\\
c&e&f
\end{bmatrix}
\mid a,b,c,d,e,f\in\mathbb{R}
\right\}
```

表示对称矩阵子空间，并令

```math
U=
\left\{
\begin{bmatrix}
a&b&c\\
0&d&e\\
0&0&f
\end{bmatrix}
\mid a,b,c,d,e,f\in\mathbb{R}
\right\}
```

表示上三角矩阵子空间。

#### 交集：两个空间共同拥有的部分

$`S\cap U`$ 包含同时属于 $`S`$ 和 $`U`$ 的矩阵。上三角矩阵的下三角元素全为零，而对称性又要求上、下三角对应元素相等，所以非对角元素只能全部为零。因此

```math
S\cap U
=\left\{
\begin{bmatrix}
a&0&0\\
0&d&0\\
0&0&f
\end{bmatrix}
\mid a,d,f\in\mathbb{R}
\right\}
=D_3.
```

一组基是 $`E_{11},E_{22},E_{33}`$，所以

```math
\dim(S\cap U)=3.
```

两个子空间的交集仍然是子空间：它们都包含零向量，而同时属于两个空间的向量做线性组合后仍同时属于两个空间。

#### 并集：通常不是子空间

$`S\cup U`$ 只是把“属于 $`S`$”或“属于 $`U`$”的矩阵放进同一个集合，并不会自动加入它们彼此相加产生的新矩阵。老师强调：

> “I'm interested in not their union but their sum.”

在对应的 $`2\times2`$ 空间中，取

```math
A=\begin{bmatrix}0&1\\1&0\end{bmatrix}\in S_2,
\qquad
B=\begin{bmatrix}0&1\\0&0\end{bmatrix}\in U_2.
```

二者都在 $`S_2\cup U_2`$ 中，但

```math
A+B=\begin{bmatrix}0&2\\1&0\end{bmatrix}
```

既不对称，也不是上三角矩阵。因此 $`A+B\notin S_2\cup U_2`$，并集对加法不封闭，通常不是子空间。只有当一个子空间包含另一个子空间时，它们的并集才仍是子空间。

#### 子空间的和：把两个空间的方向共同张成

子空间的和定义为

```math
S+U=\{\mathbf{s}+\mathbf{u}\mid\mathbf{s}\in S,\ \mathbf{u}\in U\}.
```

它不是简单的集合并集，而是收集从两个空间各取一个元素后得到的所有和。因为 $`S,U`$ 本身对标量数乘封闭，所以 $`S+U`$ 等价于把两个空间中的全部方向共同张成。若

```math
S=\mathrm{span}\{\mathbf{s}_1,\ldots,\mathbf{s}_p\},
\qquad
U=\mathrm{span}\{\mathbf{u}_1,\ldots,\mathbf{u}_q\},
```

那么

```math
S+U
=\mathrm{span}\{\mathbf{s}_1,\ldots,\mathbf{s}_p,
\mathbf{u}_1,\ldots,\mathbf{u}_q\}.
```

$`S+U`$ 总是子空间。若 $`\mathbf{x}=\mathbf{s}_1+\mathbf{u}_1`$、$`\mathbf{y}=\mathbf{s}_2+\mathbf{u}_2`$，则

```math
\alpha\mathbf{x}+\beta\mathbf{y}
=(\alpha\mathbf{s}_1+\beta\mathbf{s}_2)
+(\alpha\mathbf{u}_1+\beta\mathbf{u}_2)
\in S+U.
```

对有限维子空间，交集与和满足维数公式

```math
\boxed{
\dim(S+U)
=\dim S+\dim U-\dim(S\cap U)
}.
```

减去交集的维数，是因为共同方向在 $`\dim S+\dim U`$ 中被计算了两次。这个公式形式上类似集合的容斥公式，但这里计算的是维数，而且研究的是 $`S+U`$，不是 $`S\cup U`$。

在当前例子中：

| 空间 | 一组基所对应的自由位置 | 维数 |
| --- | --- | ---: |
| $`M_{3\times3}(\mathbb{R})`$ | 九个位置全部独立 | $`9`$ |
| $`S`$ | 三个对角位置，加三对对称位置 | $`6`$ |
| $`U`$ | 主对角线及其上方的六个位置 | $`6`$ |
| $`S\cap U=D_3`$ | 三个对角位置 | $`3`$ |

因此

```math
\dim(S+U)=6+6-3=9.
```

$`S+U`$ 是九维空间 $`M_{3\times3}(\mathbb{R})`$ 的九维子空间，所以

```math
\boxed{S+U=M_{3\times3}(\mathbb{R})}.
```

也就是说，每个 $`3\times3`$ 实矩阵都可以写成“一个对称矩阵 + 一个上三角矩阵”。这里的数字 $`6,6,3,9`$ 数的始终是基中矩阵的数量，也就是独立方向的数量，而不是简单数矩阵中出现了多少个数字。

### 7. 把矩阵展开后用消元求基

给出若干同型矩阵 $`A_1,\ldots,A_k`$，要求它们张成的矩阵空间，可以把已经学过的列空间方法直接搬过来：

1. 用同一种顺序展开每个矩阵，得到列向量 $`\Phi(A_i)`$。
2. 将这些列向量组成 $`B=[\Phi(A_1)\ \cdots\ \Phi(A_k)]`$。
3. 对 $`B`$ 消元；$`\mathrm{rank}(B)`$ 就是原矩阵张成空间的维数。
4. 找出 $`B`$ 的主元列编号，再取对应的**原矩阵**，得到一组基。

例如，令

```math
A_1=E_{11},
\qquad
A_2=E_{22},
\qquad
A_3=I_2=A_1+A_2.
```

按行展开并把结果作为列，得到

```math
B=
\begin{bmatrix}
1&0&1\\
0&0&0\\
0&0&0\\
0&1&1
\end{bmatrix}.
```

$`B`$ 的秩为 $`2`$，因此三个矩阵中有一个冗余，$`\{A_1,A_2\}`$ 是它们所张成空间的一组基。这里求的是**组装矩阵 $`B`$ 的秩**，不是把各个 $`\mathrm{rank}(A_i)`$ 相加。

### 8. 常见反例与自测

具有某种矩阵性质的集合不一定构成子空间：

| 矩阵集合 | 是否为 $`M_n(\mathbb{R})`$ 的子空间 | 原因 |
| --- | --- | --- |
| 所有对称矩阵 | 是 | 对零、加法和数乘封闭 |
| 所有对角矩阵 | 是 | 非对角零元素在线性组合后仍为零 |
| 所有迹为 $`0`$ 的矩阵 | 是 | 迹是线性的，约束是齐次的 |
| 所有迹为 $`1`$ 的矩阵 | 否 | 不包含零矩阵 |
| 所有可逆矩阵 | 否 | 不包含零矩阵，且 $`I+(-I)=\mathbf{0}`$ 破坏加法封闭 |
| 所有奇异矩阵（$`n\geq2`$） | 否 | 两个奇异矩阵相加可能可逆 |
| 所有正定实对称矩阵 | 否 | 不包含零矩阵，负数倍也不再正定 |

奇异矩阵的一个 $`2\times2`$ 反例是：$`E_{11}`$ 与 $`E_{22}`$ 都奇异，但两者之和 $`I_2`$ 可逆。**包含零向量只是子空间的必要条件，不是充分条件。**

#### 自测题

1. 一个 $`2\times2`$ 矩阵有四个位置，为什么对角矩阵空间只有二维？
2. $`\{E_{11},E_{22},I_2\}`$ 能张成 $`D_2`$ 吗？它是一组基吗？
3. 求 $`\begin{bmatrix}4&2\\2&-1\end{bmatrix}`$ 在有序基 $`(E_{11},E_{12}+E_{21},E_{22})`$ 下的坐标。
4. 所有满足 $`a_{12}=a_{21}+1`$ 的 $`2\times2`$ 矩阵构成子空间吗？
5. 求所有 $`2\times2`$ 对称且迹为零的矩阵的一组基及维数。
6. $`\mathrm{rank}(I_3)`$ 与 $`\dim(\mathrm{span}\{I_3\})`$ 分别是多少？
7. 所有 $`2\times2`$ 反对称矩阵（$`A^T=-A`$）的一般形式与维数是什么？

#### 答案与解释

1. 非对角位置固定为零，只剩两个独立线性参数；一组基是 $`E_{11},E_{22}`$。
2. 能张成，但不是基，因为 $`I_2=E_{11}+E_{22}`$，三者线性相关。
3. 坐标为 $`(4,2,-1)^T`$；同一个系数 $`2`$ 同时控制两个对称位置。
4. 不构成，因为零矩阵不满足 $`0=0+1`$，这是非齐次线性约束。
5. 一般形式为 $`\begin{bmatrix}a&b\\b&-a\end{bmatrix}`$；基可取 $`\left\{\begin{bmatrix}1&0\\0&-1\end{bmatrix},\begin{bmatrix}0&1\\1&0\end{bmatrix}\right\}`$，维数为 $`2`$。
6. 分别为 $`3`$ 和 $`1`$。前者数 $`I_3`$ 的独立列方向，后者数矩阵空间 $`\mathrm{span}\{I_3\}`$ 所需的基元素。
7. 一般形式为 $`\begin{bmatrix}0&b\\-b&0\end{bmatrix}`$，由 $`\begin{bmatrix}0&1\\-1&0\end{bmatrix}`$ 张成，维数为 $`1`$。

## 五、函数与微分方程的解空间

### 1. 函数也可以作为向量

在线性代数中，向量空间的元素也可以是函数。函数按逐点方式相加和数乘：

```math
(f+g)(x)=f(x)+g(x),
\qquad
(cf)(x)=c f(x).
```

考虑作用在二次可微实函数上的线性微分算子

```math
L(y)=y''+y.
```

微分与函数加法、标量数乘相容，因此

```math
L(c_1y_1+c_2y_2)
=c_1L(y_1)+c_2L(y_2).
```

这与矩阵变换的线性性

```math
A(c_1\mathbf{x}_1+c_2\mathbf{x}_2)
=c_1A\mathbf{x}_1+c_2A\mathbf{x}_2
```

具有完全相同的结构。

### 2. 齐次微分方程的解空间

方程

```math
y''+y=0
```

就是 $`L(y)=0`$，对应矩阵中的 $`A\mathbf{x}=\mathbf{0}`$。它的全部解组成算子 $`L`$ 的零空间：

```math
N(L)=\{y\mid L(y)=0\}.
```

如果 $`y_1,y_2\in N(L)`$，那么

```math
L(c_1y_1+c_2y_2)
=c_1L(y_1)+c_2L(y_2)
=0,
```

所以齐次线性微分方程的解集是函数空间的一个子空间。

直接计算可得

```math
(\cos x)''+\cos x
=-\cos x+\cos x
=0,
```

```math
(\sin x)''+\sin x
=-\sin x+\sin x
=0.
```

因此 $`\cos x`$ 与 $`\sin x`$ 都是齐次方程的具体解。由线性性，任意

```math
y=C_1\cos x+C_2\sin x
```

也都是解。但这一步只证明了

```math
\mathrm{span}\{\cos x,\sin x\}\subseteq N(L),
```

还不能单独证明 $`N(L)`$ 中不存在其他形式的解。

### 3. 为什么 $`\cos x,\sin x`$ 构成一组基

要证明

```math
\{\cos x,\sin x\}
```

是整个解空间的一组基，仍然必须验证**线性无关**与**张成整个空间**两个条件。

#### 线性无关

假设

```math
C_1\cos x+C_2\sin x=0
```

对所有 $`x`$ 都成立。令 $`x=0`$ 得 $`C_1=0`$；再令 $`x=\pi/2`$ 得 $`C_2=0`$。因此只有全零系数能得到零函数，$`\cos x,\sin x`$ 线性无关。

#### 张成全部解

二阶方程 $`y''+y=0`$ 的一个解由两个初始数据

```math
y(0)=a,
\qquad
y'(0)=b
```

唯一确定。对任意解 $`g`$，令

```math
a=g(0),
\qquad
b=g'(0),
```

并构造

```math
h(x)=a\cos x+b\sin x.
```

$`h`$ 满足同一个微分方程，而且

```math
h(0)=a=g(0),
\qquad
h'(0)=b=g'(0).
```

根据这个二阶线性初值问题的存在唯一性定理，具有相同初始数据的两个解必然相同，所以 $`g=h`$。这说明每个解都能写成 $`a\cos x+b\sin x`$，于是

```math
N(L)=\mathrm{span}\{\cos x,\sin x\}.
```

两个基条件现已同时满足，因此

```math
\boxed{
\{\cos x,\sin x\}
\text{ 是 }N(L)\text{ 的一组基}
},
```

并且

```math
\boxed{\dim N(L)=2}.
```

系数与初始数据直接对应：

```math
C_1=y(0),
\qquad
C_2=y'(0).
```

这两个初始数据就是解空间的两个独立自由度。更一般地，在适当的连续性条件下，$`k`$ 阶齐次线性常微分方程需要 $`k`$ 个初始数据来唯一确定一个解，其解空间通常是 $`k`$ 维的。

### 4. 与矩阵零空间和完整解的对应

矩阵方程与线性微分方程可以逐项对应：

| 矩阵语言 | 微分方程语言 |
| --- | --- |
| 矩阵 $`A`$ | 线性微分算子 $`L`$ |
| 未知向量 $`\mathbf{x}`$ | 未知函数 $`y`$ |
| $`A\mathbf{x}=\mathbf{0}`$ | $`L(y)=0`$ |
| 零空间 $`N(A)`$ | 齐次解空间 $`N(L)`$ |
| 自由变量给出的参数 | 初始数据给出的参数 |
| $`\mathbf{x}=s\mathbf{v}_1+t\mathbf{v}_2`$ | $`y=C_1\cos x+C_2\sin x`$ |

$`\cos x`$ 与 $`\sin x`$ 是两个具体的齐次解；在这一节中，更准确的角色是**线性无关的基函数**。前文所说的 particular solution（特解）主要用于非齐次方程中选定一个产生非零右端的解。

例如，把方程改成

```math
y''+y=1.
```

此时 $`y_p=1`$ 是一个特解，因为 $`y_p''+y_p=1`$。对应齐次方程的全部解仍为

```math
y_n=C_1\cos x+C_2\sin x,
```

所以非齐次方程的完整解是

```math
\boxed{
y=y_p+y_n
=1+C_1\cos x+C_2\sin x
}.
```

这正对应矩阵中的

```math
\mathbf{x}=\mathbf{x}_p+\mathbf{x}_n,
\qquad
\mathbf{x}_n\in N(A).
```

### 5. 找到候选解与证明它们是基

“怎样找到 $`\cos x,\sin x`$”和“为什么它们构成整个解空间的基”是两个不同的问题。求解时可以尝试

```math
y=e^{rx},
```

代入 $`y''+y=0`$ 得到特征方程

```math
r^2+1=0,
\qquad
r=\pm i.
```

再利用 Euler 公式得到两个实函数候选解 $`\cos x,\sin x`$。这是微分方程中**寻找解**的方法；前面完成的线性无关证明与初值唯一性论证，才是在回答它们为什么构成一组**基**。

> **验证两个函数都是解，只能说明它们的线性组合仍是解；证明它们是基，还必须证明它们线性无关并且张成全部解。**

## 六、用高斯消元识别主元结构

### 1. 消元的目的

高斯消元不只是机械地制造零，而是在把矩阵中隐藏的独立与依赖关系显露出来。

对矩阵做初等行变换，相当于左乘某个可逆矩阵 $`E`$：

```math
A\longmapsto EA.
```

若消元后发现

```math
E\mathbf{a}_2=cE\mathbf{a}_1,
```

则由 $`E`$ 可逆可得

```math
\mathbf{a}_2=c\mathbf{a}_1.
```

因此，行操作不会改变列之间的线性依赖关系，也不会改变齐次方程的解。

### 2. 行阶梯形与简化行阶梯形

为了使用同一个完整例子，令

```math
C=A^T
= \begin{bmatrix}
1&2&2&2\\
2&4&6&8\\
3&6&8&10
\end{bmatrix}.
```

向下消元得到行阶梯形（row echelon form）：

```math
C\longrightarrow
U=
\begin{bmatrix}
1&2&2&2\\
0&0&2&4\\
0&0&0&0
\end{bmatrix}.
```

$`U`$ 的主要特征是主元呈楼梯状排列，并且每个主元下面都是零。这里的主元位于第 $`1`$、$`3`$ 列，第二个主元仍为 $`2`$。

继续消元：

```math
R_2\leftarrow\frac{1}{2}R_2,
\qquad
R_1\leftarrow R_1-2R_2,
```

得到

```math
R=
\mathrm{rref}(C)
= \begin{bmatrix}
1&2&0&-2\\
0&0&1&2\\
0&0&0&0
\end{bmatrix}.
```

简化行阶梯形（reduced row echelon form，RREF）必须满足：

1. 所有非零行位于零行上方。
2. 每一行的主元都比上一行的主元更靠右。
3. 每个主元等于 $`1`$。
4. 每个主元所在列除主元外，其余元素全部为 $`0`$。

所以，把主元变成 $`1`$ 只是其中一步；还必须把主元上方的元素也消成零。RREF 与矩阵是否为方阵无关，任意尺寸的矩阵都可以化为 RREF，并且每个矩阵的 RREF 是唯一的。

### 3. 主元列与自由列

在 $`U`$ 或 $`R`$ 中，第 $`1`$、$`3`$ 列包含主元，因此它们是 **pivot columns（主元列）**；第 $`2`$、$`4`$ 列不包含主元，因此它们是 **free columns（自由列或非主元列）**。

主元列代表扫描列时出现了新的独立方向；非主元列可以由此前的主元列线性组合得到。这里需要区分两个现象：

| 消元结果 | 表示的含义 |
| --- | --- |
| 出现零行 | 某个方程是冗余约束 |
| 某列没有主元 | 该列没有提供新的独立方向 |

某个候选主元位置变成零，并不表示“这一行没有意义”；它表示在该列中找不到新的主元。

### 4. 用消元结果寻找列空间的基

主元列的编号由消元后的矩阵确定，但 $`\mathrm{Col}(C)`$ 的基必须取自**原矩阵 $`C`$ 的对应列**。

这是因为行操作保持主元位置、秩和列之间的依赖关系，却通常会改变列向量本身以及它们实际张成的列空间：

```math
\mathrm{Col}(EC)=E\mathrm{Col}(C),
```

一般并不等于 $`\mathrm{Col}(C)`$。

本例的主元列编号是 $`1,3`$，所以 $`\mathrm{Col}(C)`$ 的一组基是

```math
\left\{
\begin{bmatrix}1\\2\\3\end{bmatrix},
\begin{bmatrix}2\\6\\8\end{bmatrix}
\right\},
```

而不是直接取 $`R`$ 的第 $`1`$、$`3`$ 列作为原列空间的基。

主元的数量就是秩：

```math
r=\text{主元个数}=\mathrm{rank}(C)=2.
```

主元位置不仅筛选出列空间的独立方向，还会把未知数分成主元变量和自由变量。自由变量正是进入零空间的入口。

## 七、从自由变量到零空间

### 1. 齐次方程与零空间

当右端向量为零时，方程变成

```math
C\mathbf{x}=\mathbf{0}.
```

这叫作**齐次线性方程组**（homogeneous system）。无论 $`C`$ 是什么矩阵，$`\mathbf{x}=\mathbf{0}`$ 都是一个解，称为**平凡解**（trivial solution）。矩阵 $`C`$ 的结构决定的是除平凡解外是否还有非零解。

所有满足齐次方程的输入组成 $`C`$ 的零空间：

```math
N(C)=\{\mathbf{x}\in\mathbb{R}^n\mid C\mathbf{x}=\mathbf{0}\}.
```

从列向量角度看，零空间记录的是所有能让矩阵各列线性组合成零向量的系数组合。接下来利用消元后的主元结构求出这个空间。

零空间也是子空间。因为 $`C\mathbf{0}=\mathbf{0}`$，零向量属于其中；若 $`C\mathbf{x}_1=C\mathbf{x}_2=\mathbf{0}`$，那么

```math
C(\alpha\mathbf{x}_1+\beta\mathbf{x}_2)
=\alpha C\mathbf{x}_1+\beta C\mathbf{x}_2
=\mathbf{0},
```

所以任意线性组合仍在零空间中。

### 2. 从列的位置对应到变量

承接上一节的完整例子：

```math
C=
\begin{bmatrix}
1&2&2&2\\
2&4&6&8\\
3&6&8&10
\end{bmatrix}
\longrightarrow
U=
\begin{bmatrix}
1&2&2&2\\
0&0&2&4\\
0&0&0&0
\end{bmatrix}
```

继续把主元化为 $`1`$，并消去主元上方的元素：

```math
R=\mathrm{rref}(C)
=\begin{bmatrix}
\boxed{1}&2&0&-2\\
0&0&\boxed{1}&2\\
0&0&0&0
\end{bmatrix}.
```

$`U`$ 中两个非零行的首个非零元素分别出现在第 $`1`$、$`3`$ 列；在 $`R`$ 中，它们进一步变成了图中框出的两个主元 $`1`$。因此：

```math
\text{第 }1,3\text{ 列有主元}
\Longrightarrow
\text{主元列},
```

```math
\text{第 }2,4\text{ 列没有主元}
\Longrightarrow
\text{自由列}.
```

在方程

```math
C\mathbf{x}=\mathbf{0}
```

中，每一列对应一个未知数：

| 列 | 第1列 | 第2列 | 第3列 | 第4列 |
| --- | --- | --- | --- | --- |
| 类型 | 主元列（I） | 自由列（F） | 主元列（I） | 自由列（F） |
| 变量 | $`x_1`$ | $`x_2`$ | $`x_3`$ | $`x_4`$ |
| 变量类型 | 主元变量 | 自由变量 | 主元变量 | 自由变量 |

这里的 **I/F 是根据 RREF 中有没有主元得到的结构标签**，不是说原矩阵的第 $`1`$、$`3`$ 列本身就是单位矩阵。$`R`$ 的第 $`1`$、$`3`$ 列分别是

```math
\begin{bmatrix}1\\0\\0\end{bmatrix},
\qquad
\begin{bmatrix}0\\1\\0\end{bmatrix},
```

它们合起来呈现单位矩阵 $`I`$ 的结构；第 $`2`$、$`4`$ 列没有主元，被归入自由列部分 $`F`$。由于当前主元列和自由列交错排列，按原顺序可以记成

```math
I\quad F\quad I\quad F.
```

若把主元列排在前、自由列排在后，才会得到后文使用的紧凑分块形式

```math
R=\begin{bmatrix}I&F\end{bmatrix}.
```

自由变量（F，free）可以独立指定；主元变量由相应的单位结构（I，identity）定位，但它们不是固定常数，而是由自由变量决定。

### 3. 行操作与右端向量

研究一般方程 $`C\mathbf{x}=\mathbf{b}`$ 时，必须对增广矩阵

```math
[C\mid\mathbf{b}]
```

整体执行相同的行操作。

研究零空间时，方程按定义是

```math
C\mathbf{x}=\mathbf{0}.
```

零向量经过任何行操作仍然是零向量，所以右侧的零列通常省略，只对系数矩阵写出

```math
C\longrightarrow U\longrightarrow R.
```

这些行操作可逆，因此

```math
N(C)=N(U)=N(R).
```

这里的 $`R`$ 只是系数矩阵的 RREF，并不是增广矩阵。

### 4. 从 RREF 读出齐次方程的解

由

```math
R=
\begin{bmatrix}
1&2&0&-2\\
0&0&1&2\\
0&0&0&0
\end{bmatrix}
```

可得

```math
\begin{cases}
x_1+2x_2-2x_4=0,\\
x_3+2x_4=0.
\end{cases}
```

令自由变量

```math
x_2=s,
\qquad
x_4=t,
```

则主元变量为

```math
x_1=-2s+2t,
\qquad
x_3=-2t.
```

因此所有解是

```math
\mathbf{x}
= \begin{bmatrix}
-2s+2t\\
s\\
-2t\\
t
\end{bmatrix}
= s
\begin{bmatrix}
-2\\1\\0\\0
\end{bmatrix}
+
t
\begin{bmatrix}
2\\0\\-2\\1
\end{bmatrix}.
```

### 5. 特殊解与零空间的基

零空间定义为

```math
N(C)=\{\mathbf{x}\in\mathbb{R}^4\mid C\mathbf{x}=\mathbf{0}\}.
```

分别令一个自由变量为 $`1`$、其余自由变量为 $`0`$，得到 **special solutions（特殊解）**：

```math
\mathbf{v}_1=
\begin{bmatrix}-2\\1\\0\\0\end{bmatrix},
\qquad
\mathbf{v}_2=
\begin{bmatrix}2\\0\\-2\\1\end{bmatrix}.
```

所有解都是这两个特殊解的线性组合，所以

```math
N(C)
= \mathrm{span}
\left\{
\mathbf{v}_1,\mathbf{v}_2
\right\}.
```

$`\mathbf{v}_1,\mathbf{v}_2`$ 构成零空间的一组基。参数 $`s,t`$ 只是任意实数系数；自由变量有几个，就会得到几个基本的特殊解方向。

这里可以把自由变量到零空间维数的过程完整写成：

```math
\text{两个自由变量}
\Longrightarrow
\text{两个独立参数 }s,t
\Longrightarrow
\text{两个特殊解}
\Longrightarrow
\text{两个零空间基向量}.
```

每个特殊解都由“一个自由变量取 $`1`$，其余自由变量取 $`0`$”得到。例如，取 $`s=1,t=0`$ 得到 $`\mathbf{v}_1`$，取 $`s=0,t=1`$ 得到 $`\mathbf{v}_2`$。因此 $`\mathbf{v}_1`$ 最后一个分量为 $`0`$，是因为这次令 $`t=0`$，并不是为了凑够四个分量而补上的零。

特殊解能够张成全部解；它们又分别对应相互独立的自由参数，因此线性无关。二者共同保证这些特殊解构成零空间的一组基。

零空间中的向量记录的是矩阵各列之间的依赖关系。例如

```math
C\mathbf{v}_1=\mathbf{0}
\quad\Longleftrightarrow\quad
-2\mathbf{c}_1+\mathbf{c}_2=\mathbf{0},
```

而

```math
C\mathbf{v}_2=\mathbf{0}
\quad\Longleftrightarrow\quad
2\mathbf{c}_1-2\mathbf{c}_3+\mathbf{c}_4=\mathbf{0}.
```

因此，零空间可以理解为所有“让矩阵各列抵消成零的系数组合”。

### 6. RREF 的分块形式

在 RREF 中，把主元列与自由列分别集中排列，并忽略底部零行，可以把非零部分写成

```math
R=\begin{bmatrix}I&F\end{bmatrix}.
```

$`I`$ 是主元列形成的单位矩阵块，$`F`$ 是自由列组成的矩阵块。真正可以自由选择的是与 $`F`$ 对应的变量 $`\mathbf{x}_F`$，不是矩阵 $`F`$ 本身。

把变量也按主元变量、自由变量分组：

```math
\mathbf{x}
= \begin{bmatrix}
\mathbf{x}_P\\
\mathbf{x}_F
\end{bmatrix}.
```

齐次方程成为

```math
\begin{bmatrix}I&F\end{bmatrix}
\begin{bmatrix}
\mathbf{x}_P\\
\mathbf{x}_F
\end{bmatrix}
= \mathbf{0}.
```

于是

```math
\mathbf{x}_P+F\mathbf{x}_F=\mathbf{0},
```

所以

```math
\mathbf{x}_P=-F\mathbf{x}_F.
```

负号只来自移项。整个解可以写为

```math
\begin{bmatrix}
\mathbf{x}_P\\
\mathbf{x}_F
\end{bmatrix}
= \begin{bmatrix}
-F\\
I
\end{bmatrix}
\mathbf{x}_F.
```

矩阵

```math
\begin{bmatrix}-F\\I\end{bmatrix}
```

的各列就是零空间的特殊解，也构成零空间的一组基。

这个紧凑公式有一个重要前提：列和变量已经按“主元在前、自由变量在后”重新排列。当前例子的顺序是

```math
x_1,\ x_2,\ x_3,\ x_4
\quad\longrightarrow\quad
x_1,\ x_3\mid x_2,\ x_4.
```

如果主元列和自由列在原矩阵中交错排列，最后必须把解向量的分量恢复到原变量顺序，不能直接机械地上下拼接。

自由变量的数量就是零空间的维数。这个数量与主元数之间的关系，把零空间、秩以及转置后的矩阵联系起来。

## 八、秩、零度与转置

### 1. 秩与自由变量数量

若

```math
C\in\mathbb{R}^{m\times n},
\qquad
\mathrm{rank}(C)=r,
```

矩阵有 $`n`$ 列，所以未知向量 $`\mathbf{x}`$ 有 $`n`$ 个分量。主元变量有 $`r`$ 个，剩下的自由变量有 $`n-r`$ 个。每个自由变量产生一个独立参数和一个基本的特殊解方向，因此

```math
\mathrm{nullity}(C)
= \dim N(C)
= n-r.
```

这条等式可以理解为：

```math
\boxed{
\text{自由变量数量}
=\text{零空间基向量数量}
=\dim N(C)
=n-r
}.
```

这就是秩－零度定理：

```math
\dim\bigl(\mathrm{Col}(C)\bigr)+\dim N(C)
=r+(n-r)
=n,
```

也就是

```math
\mathrm{rank}(C)+\mathrm{nullity}(C)=n.
```

当前例子中 $`n=4,r=2`$，所以

```math
\dim N(C)=4-2=2.
```

这里尤其要区分“向量有几个分量”与“空间有几个独立方向”。当前矩阵 $`C`$ 是 $`3\times4`$ 矩阵，因此

```math
C:\mathbb{R}^4\longrightarrow\mathbb{R}^3.
```

输入 $`\mathbf{x}`$ 必须有四个分量，所以每个零空间向量也都有四个分量：

```math
N(C)\subseteq\mathbb{R}^4.
```

但 $`C`$ 只有两个自由变量，零空间的一组基只有两个向量，因此

```math
\dim N(C)=2.
```

同理，$`C`$ 的列向量有三个分量，所以

```math
\mathrm{Col}(C)\subseteq\mathbb{R}^3,
\qquad
\dim\bigl(\mathrm{Col}(C)\bigr)=r=2.
```

所以“位于 $`\mathbb{R}^4`$ 中”不等于“这个子空间是四维的”。前者说明向量的格式和环境空间，后者才说明子空间拥有多少个独立方向。

没有自由变量时，齐次系统只有平凡解；只要存在自由变量，齐次系统就有无穷多个解。

### 2. 转置与秩

矩阵转置会交换行和列，但不会改变秩：

```math
\mathrm{rank}(A)=\mathrm{rank}(A^T).
```

其本质是行秩等于列秩。对前面的矩阵，

```math
\mathrm{rank}(A)
= \mathrm{rank}(A^T)
=2.
```

不过，转置前后的零空间通常不同。因为

```math
A:\mathbb{R}^3\to\mathbb{R}^4,
\qquad
A^T:\mathbb{R}^4\to\mathbb{R}^3,
```

所以

```math
N(A)\subseteq\mathbb{R}^3,
\qquad
N(A^T)\subseteq\mathbb{R}^4.
```

本例中

```math
\dim N(A)=3-2=1,
\qquad
\dim N(A^T)=4-2=2.
```

秩相同不代表零空间相同。

转置不仅给出另一个零空间，还把矩阵的行变成列。于是，列空间、零空间以及转置后的两个对应空间自然组成矩阵的四个基本子空间。

## 九、矩阵的四个基本子空间

### 1. 四个空间的总图

设

```math
A\in\mathbb{R}^{m\times n},
\qquad
\mathrm{rank}(A)=r.
```

矩阵 $`A`$ 的四个基本子空间（four fundamental subspaces）是：

| 基本子空间 | 记号 | 所在的环境空间 | 维数 | 核心含义 |
| --- | --- | --- | ---: | --- |
| 列空间 | $`\mathrm{Col}(A)`$ | $`\mathbb{R}^m`$ | $`r`$ | $`A`$ 能产生的全部输出 |
| 零空间 | $`N(A)`$ | $`\mathbb{R}^n`$ | $`n-r`$ | 被 $`A`$ 变成零向量的全部输入 |
| 行空间 | $`\mathrm{Row}(A)=\mathrm{Col}(A^T)`$ | $`\mathbb{R}^n`$ | $`r`$ | $`A`$ 的各行所张成的空间 |
| 左零空间 | $`N(A^T)`$ | $`\mathbb{R}^m`$ | $`m-r`$ | 与 $`A`$ 的全部列正交的方向 |

它们分布在矩阵映射的两侧：

```math
\begin{array}{ccc}
\mathbb{R}^n & \xrightarrow{\quad A\quad} & \mathbb{R}^m\\[2mm]
\mathrm{Col}(A^T)\ (r) && \mathrm{Col}(A)\ (r)\\[1mm]
N(A)\ (n-r) && N(A^T)\ (m-r)
\end{array}
```

左边是输入所在的 $`\mathbb{R}^n`$：矩阵的每一行有 $`n`$ 个分量，零空间中的输入也有 $`n`$ 个分量。右边是输出所在的 $`\mathbb{R}^m`$：矩阵的每一列有 $`m`$ 个分量，左零空间中的向量也有 $`m`$ 个分量。

> **四个基本子空间不是四套互不相关的新知识，而是把列空间、零空间、转置、秩、基与维数汇合到同一张图中。**

### 2. 行空间与行秩

把 $`A`$ 的行向量转置后，它们正是 $`A^T`$ 的列，因此

```math
\mathrm{Row}(A)=\mathrm{Col}(A^T).
```

行空间位于 $`\mathbb{R}^n`$。它的维数称为行秩；列空间的维数称为列秩。高斯消元得到的同一批 $`r`$ 个主元同时给出独立行和独立列的数量，所以

```math
\boxed{
\text{行秩}
=\text{列秩}
=\mathrm{rank}(A)
=r
}.
```

因此

```math
\dim\bigl(\mathrm{Col}(A^T)\bigr)
=\dim\bigl(\mathrm{Col}(A)\bigr)
=r.
```

这里只能说两个空间的**维数相同**，不能说它们是同一个空间。$`\mathrm{Col}(A^T)`$ 位于 $`\mathbb{R}^n`$，$`\mathrm{Col}(A)`$ 位于 $`\mathbb{R}^m`$；当 $`m\neq n`$ 时，它们甚至位于不同的环境空间。

#### 从相同行到列相关

另取一个 $`3\times3`$ 方阵

```math
B=
\begin{bmatrix}
1&2&3\\
2&4&5\\
2&4&5
\end{bmatrix}.
```

第二、三行相同，因此

```math
R_3-R_2=\mathbf{0}
```

给出了一个非平凡的行关系，说明各行线性相关。执行

```math
R_3\leftarrow R_3-R_2
```

会出现一个零行，所以最多只有两个主元：

```math
\mathrm{rank}(B)\leq2<3.
```

行相关之所以能进一步推出列相关，桥梁正是行秩等于列秩。独立行不足三个意味着秩小于三，也意味着独立列不足三个，因此三列必然线性相关：

> “It has two identical rows. Its rows are obviously dependent. And that makes the columns dependent.”

```math
\boxed{
\text{两行相同}
\Longrightarrow
\text{行相关}
\Longrightarrow
\mathrm{rank}(B)<3
\Longrightarrow
 B\text{ 不可逆}
\Longrightarrow
\text{列相关}
}.
```

从主元角度看，零行使 $`B`$ 最多只有两个主元，不可能每列都有主元；从可逆性角度看，方阵的秩小于阶数，所以 RREF 不可能是单位矩阵。这是同一事实的两种表述。

从零空间也能看到同一件事。因为 $`n=3`$ 且 $`r<3`$，所以 $`n-r>0`$，齐次方程 $`B\mathbf{x}=\mathbf{0}`$ 有自由变量和非零解。写成列组合就是

```math
x_1\mathbf{b}_1+x_2\mathbf{b}_2+x_3\mathbf{b}_3
=\mathbf{0},
\qquad
\mathbf{x}\neq\mathbf{0},
```

这正是三列线性相关的定义。

### 3. 左零空间

对转置矩阵求零空间，得到第四个基本子空间：

```math
N(A^T)
=\{\mathbf{y}\in\mathbb{R}^m\mid A^T\mathbf{y}=\mathbf{0}\}.
```

将等式转置，并使用 $`(BC)^T=C^TB^T`$，可得

```math
A^T\mathbf{y}=\mathbf{0}
\quad\Longleftrightarrow\quad
\mathbf{y}^TA=\mathbf{0}^T.
```

在后一种写法中，$`\mathbf{y}^T`$ 从矩阵左边相乘，所以 $`N(A^T)`$ 称为 **left null space（左零空间）**。

$`A^T`$ 有 $`m`$ 列，并且

```math
\mathrm{rank}(A^T)=\mathrm{rank}(A)=r,
```

所以秩－零度关系给出

```math
\dim N(A^T)=m-r.
```

### 4. 两对正交关系

若 $`\mathbf{x}\in N(A)`$，则 $`A\mathbf{x}=\mathbf{0}`$。把 $`A`$ 的各行记为 $`\mathbf{r}_1^T,\ldots,\mathbf{r}_m^T`$，就有

```math
A\mathbf{x}
=\begin{bmatrix}
\mathbf{r}_1^T\mathbf{x}\\
\vdots\\
\mathbf{r}_m^T\mathbf{x}
\end{bmatrix}
=\mathbf{0}.
```

因此 $`\mathbf{x}`$ 与每一个行向量的点积都为零，零空间与行空间正交：

```math
N(A)\perp\mathrm{Col}(A^T).
```

同理，若 $`\mathbf{y}\in N(A^T)`$，则 $`A^T\mathbf{y}=\mathbf{0}`$，所以 $`\mathbf{y}`$ 与 $`A`$ 的每一列正交：

```math
N(A^T)\perp\mathrm{Col}(A).
```

每一对空间的维数又恰好填满所在的环境空间：

```math
\dim\bigl(\mathrm{Col}(A^T)\bigr)+\dim N(A)
=r+(n-r)=n,
```

```math
\dim\bigl(\mathrm{Col}(A)\bigr)+\dim N(A^T)
=r+(m-r)=m.
```

因此可以写成两组正交分解：

```math
\mathbb{R}^n
=\mathrm{Col}(A^T)\mathbin{\oplus}N(A),
\qquad
\mathbb{R}^m
=\mathrm{Col}(A)\mathbin{\oplus}N(A^T).
```

这里的 $`\oplus`$ 表示两个互相正交、只在零向量处相交的子空间共同组成整个环境空间。

### 5. 用消元矩阵寻找左零空间

一次初等行变换可以表示为在左侧乘一个初等矩阵。若从 $`A`$ 到其 RREF 共执行了若干次行变换，把相应的初等矩阵依次记为 $`E_1,\ldots,E_k`$，则

```math
R=E_k\cdots E_2E_1A.
```

把全部行变换合并为

```math
E=E_k\cdots E_2E_1,
```

便得到老师板书中的主线：

```math
\boxed{EA=R}.
```

这里四个矩阵的角色不同：$`A`$ 是原矩阵，$`R=\mathrm{rref}(A)`$ 是消元结果，$`I_m`$ 表示尚未进行任何操作，$`E`$ 是把全部行变换打包后的总行变换矩阵。

为了同时算出 $`E`$，在 $`A`$ 右侧附加单位矩阵，并对两部分执行相同的行变换：

```math
[A\mid I_m]
\longrightarrow
[R\mid E].
```

其原因是

```math
E[A\mid I_m]
=[EA\mid EI_m]
=[R\mid E].
```

> **左半边 $`A\to R`$ 记录矩阵变成了什么；右半边 $`I_m\to E`$ 记录刚才对它做了什么。**

若 $`R`$ 的第 $`i`$ 行为零，而 $`E`$ 的对应行为 $`\mathbf{e}_i^T`$，由 $`EA=R`$ 可知

```math
\mathbf{e}_i^TA=\mathbf{0}^T,
```

所以

```math
A^T\mathbf{e}_i=\mathbf{0},
\qquad
\mathbf{e}_i\in N(A^T).
```

$`R`$ 一共有 $`m-r`$ 个零行，$`E`$ 中与这些零行对应的各行转置后，构成 $`N(A^T)`$ 的一组基。这些向量具体记录了原矩阵的哪些行以什么系数组合成零行。

这也解释了熟悉的求逆方法。只有当 $`A`$ 是可逆方阵时，$`R=I`$，于是

```math
EA=I
\quad\Longrightarrow\quad
E=A^{-1},
```

从而

```math
[A\mid I]\longrightarrow[I\mid A^{-1}].
```

一般情况下 $`E`$ 只是总行变换矩阵，并不等于 $`A^{-1}`$。

## 十、用列空间与零空间描述完整解

### 1. 特解与零空间解

假设 $`A\mathbf{x}=\mathbf{b}`$ 有解，并且已经找到其中一个解 $`\mathbf{x}_p`$：

```math
A\mathbf{x}_p=\mathbf{b}.
```

$`\mathbf{x}_p`$ 称为 **particular solution（特解）**。再取零空间中的任意向量 $`\mathbf{x}_n`$：

```math
\mathbf{x}_n\in N(A),
\qquad
A\mathbf{x}_n=\mathbf{0}.
```

利用线性性可得

```math
A(\mathbf{x}_p+\mathbf{x}_n)
=A\mathbf{x}_p+A\mathbf{x}_n
=\mathbf{b}+\mathbf{0}
=\mathbf{b}.
```

因此，在特解上加任意零空间向量，仍然是原方程的解。这里能加的不是任意向量，而只能是 $`N(A)`$ 中的向量。

### 2. 为什么这包含全部解

若 $`\mathbf{x}`$ 是 $`A\mathbf{x}=\mathbf{b}`$ 的任意一个解，那么

```math
A\mathbf{x}=\mathbf{b},
\qquad
A\mathbf{x}_p=\mathbf{b}.
```

两式相减：

```math
A(\mathbf{x}-\mathbf{x}_p)=\mathbf{0}.
```

所以

```math
\mathbf{x}-\mathbf{x}_p\in N(A).
```

令 $`\mathbf{x}_n=\mathbf{x}-\mathbf{x}_p`$，便得到

```math
\boxed{
\mathbf{x}=\mathbf{x}_p+\mathbf{x}_n,
\qquad
\mathbf{x}_n\in N(A)
}.
```

这说明所有解，而且只有所有解，都属于集合

```math
\boxed{
\{\mathbf{x}:A\mathbf{x}=\mathbf{b}\}
=\mathbf{x}_p+N(A)
}.
```

因此可以概括为

```math
\text{complete solution（通解）}
= \text{particular solution（特解）}
+
\text{null-space solution（零空间解）}.
```

### 3. 自由变量在完整解中的作用

求一个方便的特解时，通常先把所有自由变量设为 $`0`$，再计算主元变量。这样得到的 $`\mathbf{x}_p`$ 只负责产生目标输出：

```math
A\mathbf{x}_p=\mathbf{b}.
```

自由变量能够产生的全部变化集中在 $`\mathbf{x}_n`$ 中，而这些变化不会影响输出：

```math
A\mathbf{x}_n=\mathbf{0}.
```

从列向量视角看，$`\mathbf{x}_p`$ 是一套把矩阵各列组合成 $`\mathbf{b}`$ 的系数；$`\mathbf{x}_n`$ 是一套让各列互相抵消成零的系数。两套系数相加后，输出仍然是 $`\mathbf{b}`$。

### 4. 解集的几何形状

零空间 $`N(A)`$ 一定经过原点，是一个子空间。若方程有一个特解 $`\mathbf{x}_p`$，则非齐次方程的解集是

```math
\mathbf{x}_p+N(A),
```

也就是把零空间整体平移到经过 $`\mathbf{x}_p`$ 的位置。

- 若 $`N(A)`$ 是一条直线，解集是经过 $`\mathbf{x}_p`$、与该直线平行的直线。
- 若 $`N(A)`$ 是一个平面，解集是经过 $`\mathbf{x}_p`$、与该平面平行的平面。

这种平移后的集合称为**仿射空间**（affine space）。当 $`\mathbf{b}\neq\mathbf{0}`$ 时，$`\mathbf{x}=\mathbf{0}`$ 不可能满足方程，因此解集一定不是线性子空间：若无解，解集为空；若有特解，则解集是 $`\mathbf{x}_p+N(A)`$ 这样的仿射子空间。当 $`\mathbf{b}=\mathbf{0}`$ 时，解集就是 $`N(A)`$，它是线性子空间。

若 $`\mathbf{x}_1,\mathbf{x}_2`$ 都是 $`A\mathbf{x}=\mathbf{b}`$ 的解，则

```math
A(\mathbf{x}_1-\mathbf{x}_2)=\mathbf{0},
\qquad
A(\mathbf{x}_1+\mathbf{x}_2)=2\mathbf{b}.
```

所以两个解之差属于零空间，但两个解之和通常不再是原方程的解。若 $`\alpha+\beta=1`$，则 $`\alpha\mathbf{x}_1+\beta\mathbf{x}_2`$ 仍是解；这种系数和为 $`1`$ 的组合称为**仿射组合**，不同于允许任意系数的线性组合。

完整解公式把问题分成了两步：列空间决定特解是否存在，零空间决定能否在特解之外继续变化。接下来只需比较 $`r,m,n`$，就能统一判断解的数量。

## 十一、用秩判断解的数量

### 1. 两个核心判断

设

```math
A\in\mathbb{R}^{m\times n},
\qquad
r=\mathrm{rank}(A).
```

其中 $`m`$ 是行数和方程数，$`n`$ 是列数和未知数数，$`r`$ 是主元数量。

解的结构由两个条件分别控制：

```math
r=m
\quad\Longleftrightarrow\quad
\text{每一行都有主元}
\quad\Longleftrightarrow\quad
\mathrm{Col}(A)=\mathbb{R}^m.
```

所以 $`r=m`$ 保证 $`A\mathbf{x}=\mathbf{b}`$ 对每个 $`\mathbf{b}\in\mathbb{R}^m`$ 都有解，控制的是**存在性**。

另一方面，

```math
r=n
\quad\Longleftrightarrow\quad
\text{每一列都有主元}
\quad\Longleftrightarrow\quad
N(A)=\{\mathbf{0}\}.
```

所以 $`r=n`$ 保证没有自由变量，方程只要有解就必然唯一，控制的是**唯一性**。

### 2. 四种典型情形

| 秩与尺寸的关系 | 分组后的 RREF 结构 | 自由变量 | 是否对每个 $`\mathbf{b}`$ 有解 | 某个 $`A\mathbf{x}=\mathbf{b}`$ 的解数 |
| --- | --- | ---: | --- | --- |
| $`r=m=n`$ | $`I`$ | $`0`$ | 是 | 恰好一个 |
| $`r=n<m`$ | $`\begin{bmatrix}I\\0\end{bmatrix}`$ | $`0`$ | 不一定 | $`0`$ 或 $`1`$ |
| $`r=m<n`$ | $`\begin{bmatrix}I&F\end{bmatrix}`$ | $`n-r>0`$ | 是 | 无穷多个 |
| $`r<m`$ 且 $`r<n`$ | $`\begin{bmatrix}I&F\\0&0\end{bmatrix}`$ | $`n-r>0`$ | 不一定 | $`0`$ 或无穷多个 |

表中的 $`I`$ 与 $`F`$ 是把主元列和自由列重新分组后的抽象结构；它们在原矩阵中可能交错排列。

#### 满秩方阵：$`r=m=n`$

每一行和每一列都有主元，因此所有 $`\mathbf{b}`$ 都可到达，同时没有自由变量。于是每个 $`\mathbf{b}`$ 都有唯一解。

#### 满列秩高矩阵：$`r=n<m`$

每一列都有主元，所以没有自由变量；但不是每一行都有主元，因此列空间不能填满 $`\mathbb{R}^m`$。某个方程可能无解，也可能有唯一解，但不可能有无穷多个解。

#### 满行秩宽矩阵：$`r=m<n`$

每一行都有主元，所以每个 $`\mathbf{b}`$ 都有解；同时 $`n-r>0`$，存在自由变量，因此每个 $`\mathbf{b}`$ 都有无穷多个解。

#### 行列都不满秩：$`r<m`$ 且 $`r<n`$

不是每个 $`\mathbf{b}`$ 都在列空间中，所以某些方程无解；一旦有解，又会因为存在自由变量而有无穷多个解。

### 3. 满秩方阵与唯一解

当

```math
r=m=n
```

时，$`A`$ 是满秩方阵。这里“没有任何”指的是没有自由变量、没有非零的零空间解，而不是没有特解。

因为 $`r=n`$，所以

```math
N(A)=\{\mathbf{0}\}.
```

完整解公式退化为

```math
\mathbf{x}=\mathbf{x}_p+\mathbf{0}=\mathbf{x}_p.
```

同时，因为 $`r=m`$，任意 $`\mathbf{b}`$ 都在列空间中，所以特解总是存在。因此每个右端向量都有且只有一个解。

满秩方阵的 RREF 是单位矩阵：

```math
\mathrm{rref}(A)=I.
```

注意，这是说 $`A`$ 的 RREF 等于 $`I`$，并不是说原矩阵 $`A`$ 本身一定等于 $`I`$。

### 4. 可逆矩阵

对 $`n\times n`$ 方阵，满秩还意味着 $`A`$ 可逆。此时 $`A^{-1}`$ 存在，而且

```math
A\mathbf{x}=\mathbf{b}
\quad\Longrightarrow\quad
\mathbf{x}=A^{-1}\mathbf{b}.
```

例如

```math
A=
\begin{bmatrix}
1&2\\
3&1
\end{bmatrix}
```

满足

```math
\det(A)=1\cdot1-2\cdot3=-5\neq0,
```

所以它可逆，并且对任意 $`\mathbf{b}\in\mathbb{R}^2`$ 都有唯一解。

对于 $`n\times n`$ 方阵，下面这些说法彼此等价：

```math
\mathrm{rank}(A)=n
\Longleftrightarrow
\text{每行、每列都有主元}
\Longleftrightarrow
\mathrm{rref}(A)=I
```

```math
\Longleftrightarrow
\text{各行线性无关}
\Longleftrightarrow
\text{各列线性无关}
\Longleftrightarrow
\text{各列构成 }\mathbb{R}^n\text{ 的一组基}
```

```math
\Longleftrightarrow
N(A)=\{\mathbf{0}\}
\Longleftrightarrow
N(A^T)=\{\mathbf{0}\}
\Longleftrightarrow
\mathrm{Col}(A)=\mathbb{R}^n
\Longleftrightarrow
A^{-1}\text{ 存在}
```

```math
\Longleftrightarrow
A\mathbf{x}=\mathbf{b}
\text{ 对每个 }\mathbf{b}\in\mathbb{R}^n
\text{ 都有唯一解}.
```

若把 $`n`$ 个 $`n`$ 维向量作为列组成方阵

```math
A=\begin{bmatrix}
\mathbf{v}_1&\cdots&\mathbf{v}_n
\end{bmatrix},
```

那么

```math
\boxed{
\mathbf{v}_1,\ldots,\mathbf{v}_n
\text{ 构成 }\mathbb{R}^n\text{ 的一组基}
\quad\Longleftrightarrow\quad
A\text{ 可逆}
}.
```

因此，对方阵而言，只要有两行相同，就会破坏行的线性无关性，使秩小于 $`n`$；同一个秩也迫使列线性相关，矩阵因而不可逆。

### 5. 解的数量为什么只有三种

线性方程组的解数只能是

```math
0,\qquad1,\qquad\infty.
```

如果 $`\mathbf{x}^{(1)}`$ 和 $`\mathbf{x}^{(2)}`$ 是两个不同的解，那么

```math
A(\mathbf{x}^{(1)}-\mathbf{x}^{(2)})=\mathbf{0}.
```

令

```math
\mathbf{v}=\mathbf{x}^{(1)}-\mathbf{x}^{(2)}\neq\mathbf{0},
```

则对任意 $`c\in\mathbb{R}`$，

```math
A(\mathbf{x}^{(1)}+c\mathbf{v})
=\mathbf{b}+c\mathbf{0}
=\mathbf{b}.
```

因此，只要出现两个不同的解，就会沿着非零零空间方向产生无穷多个解，不可能恰好只有 $`2`$ 个、$`3`$ 个或其他有限多个解。

## 十二、当前课程的统一逻辑

### 1. 两个环境空间与四个基本子空间

对于 $`C\in\mathbb{R}^{m\times n}`$：

```math
\mathbb{R}^n\xrightarrow{\quad C\quad}\mathbb{R}^m.
```

四个基本子空间从两侧描述同一个矩阵：

| 所在位置 | 空间 | 核心问题 |
| --- | --- | --- |
| $`\mathbb{R}^n`$ | 行空间 $`\mathrm{Col}(C^T)`$ | $`C`$ 的行能够张成哪些输入方向？ |
| $`\mathbb{R}^n`$ | 零空间 $`N(C)`$ | 哪些输入 $`\mathbf{x}`$ 会被 $`C`$ 送到零向量？ |
| $`\mathbb{R}^m`$ | 列空间 $`\mathrm{Col}(C)`$ | 哪些输出 $`\mathbf{b}`$ 能由 $`C`$ 产生？ |
| $`\mathbb{R}^m`$ | 左零空间 $`N(C^T)`$ | 哪些输出端方向与 $`C`$ 的全部列正交？ |

因此：

```math
C\mathbf{x}=\mathbf{b}\text{ 是否有解}
\quad\text{由列空间决定；}
```

```math
C\mathbf{x}=\mathbf{b}\text{ 若有解，是否唯一}
\quad\text{由零空间决定。}
```

若 $`\mathbf{x}_p`$ 是 $`C\mathbf{x}=\mathbf{b}`$ 的一个特解，那么所有解都可以写成

```math
\mathbf{x}=\mathbf{x}_p+\mathbf{x}_n,
\qquad
\mathbf{x}_n\in N(C).
```

### 2. 整堂课的逻辑链

向量空间的元素不局限于列向量。把固定大小的矩阵作为元素时，同样沿用下面这条主线：

```math
\text{矩阵线性组合}
\longrightarrow
\text{矩阵子空间}
\longrightarrow
\text{矩阵组成的基}
\longrightarrow
\text{矩阵空间的维数}.
```

这里必须与单个矩阵的秩分开：

```math
\mathrm{rank}(A)
=\dim\bigl(\mathrm{Col}(A)\bigr),
\qquad
\dim\bigl(\mathrm{span}\{A\}\bigr)=1
\quad(A\neq\mathbf{0}).
```

两个子空间之间，交集保留共同方向，子空间之和把双方方向共同张成：

```math
S\cap U
=\text{共同部分},
\qquad
S+U
=\{\mathbf{s}+\mathbf{u}\mid\mathbf{s}\in S,\ \mathbf{u}\in U\}.
```

```math
\dim(S+U)
=\dim S+\dim U-\dim(S\cap U).
```

函数作为向量时，线性微分算子的齐次解空间也是零空间：

```math
L(y)=y''+y,
\qquad
N(L)=\mathrm{span}\{\cos x,\sin x\},
\qquad
\dim N(L)=2.
```

```math
\text{非齐次完整解}
=\text{一个特解}
+\text{对应齐次解空间}.
```

```math
\text{线性组合}
\longrightarrow
\text{张成子空间}
\longrightarrow
\text{矩阵各列张成列空间}
```

```math
\text{线性无关排除冗余}
\quad+\quad
\text{张成保证完整覆盖}
\longrightarrow
\text{基}
\longrightarrow
\text{维数}
```

```math
A\mathbf{x}=\mathbf{b}\text{ 有解}
\Longleftrightarrow
\mathbf{b}\in\mathrm{Col}(A)
```

```math
\text{高斯消元}
\longrightarrow
\text{主元位置}
\longrightarrow
\text{列空间的基}
\longrightarrow
\dim\bigl(\mathrm{Col}(A)\bigr)=\mathrm{rank}(A)=r
```

```math
\text{非主元列}
\longrightarrow
\text{自由变量}
\longrightarrow
\text{特殊解}
\longrightarrow
\text{零空间的基}
\longrightarrow
\dim N(A)=n-r
```

```math
\dim\bigl(\mathrm{Col}(A)\bigr)+\dim N(A)
=r+(n-r)=n
```

转置把同一套结构带到另外两个基本子空间：

```math
\mathrm{Row}(A)=\mathrm{Col}(A^T),
\qquad
\dim\bigl(\mathrm{Col}(A^T)\bigr)=r,
\qquad
\dim N(A^T)=m-r.
```

```math
N(A)\perp\mathrm{Col}(A^T),
\qquad
N(A^T)\perp\mathrm{Col}(A).
```

消元既显露主元结构，也能记录产生零行的行关系：

```math
[A\mid I_m]\longrightarrow[R\mid E],
\qquad
EA=R.
```

```math
\mathbf{b}\in\mathrm{Col}(A)
\longrightarrow
\text{找到一个特解 }\mathbf{x}_p
\longrightarrow
\mathbf{x}=\mathbf{x}_p+\mathbf{x}_n,
\quad \mathbf{x}_n\in N(A)
```

```math
r=m\Longrightarrow\text{每个右端向量都有解},
\qquad
r=n\Longrightarrow\text{有解时解唯一}.
```

另一条并行主线是把一整个矩阵或函数当作向量空间中的元素：对角矩阵空间、对称矩阵空间与齐次微分方程的解空间都使用同样的线性组合、基与维数概念。矩阵空间的维数数的是基中有几个矩阵元素，不能与单个矩阵的秩混淆；函数解空间的维数数的是需要几个独立基函数，不能只靠验证几个候选函数是解来确定。

最终，列空间描述矩阵能到达哪里，零空间描述矩阵会丢失哪些输入方向；行空间概括矩阵对输入进行检测的方向，左零空间记录与全部列正交的输出端方向。特解负责到达目标输出，零空间负责描述不改变输出的全部自由变化，而主元、秩、转置和消元矩阵把这些结构联系在一起。

### 3. 术语对照

| 英文 | 中文 | 本节含义 |
| --- | --- | --- |
| scalar | 标量 | 与向量相乘的普通数 |
| linear combination | 线性组合 | 用一组具体系数对向量进行数乘后相加 |
| span | 张成 | 一组向量所有线性组合的集合 |
| linearly independent | 线性无关 | 只有全零系数才能使线性组合等于零向量 |
| linearly dependent | 线性相关 | 存在不全为零的系数使线性组合等于零向量 |
| basis | 基 | 同时线性无关并张成整个空间的一组向量 |
| dimension | 维数 | 空间任意一组基所含向量的数量 |
| coordinate | 坐标 | 一个向量在指定有序基下的唯一系数列 |
| matrix space | 矩阵空间 | 以固定大小矩阵作为元素的向量空间 |
| diagonal matrix space | 对角矩阵空间 | 所有固定阶数对角矩阵组成的子空间 |
| symmetric matrix space | 对称矩阵空间 | 所有满足 $`A^T=A`$ 的固定阶数矩阵组成的子空间 |
| linear isomorphism | 线性同构 | 保持线性运算的一一对应，表示结构相同而非集合相同 |
| intersection | 交集 | $`S\cap U`$，同时属于两个子空间的元素组成的子空间 |
| union | 并集 | $`S\cup U`$，简单合并两个集合，通常不是子空间 |
| sum of subspaces | 子空间的和 | $`S+U`$，双方元素之和构成的子空间 |
| function space | 函数空间 | 以函数作为向量、按逐点方式定义加法与数乘的空间 |
| differential operator | 微分算子 | 把函数映射到函数的算子；本例 $`L(y)=y''+y`$ |
| solution space | 解空间 | 齐次线性方程全部解组成的向量空间 |
| initial condition | 初始条件 | 用函数值及其导数值唯一确定微分方程解的数据 |
| column space | 列空间 | 矩阵所有可能输出的集合 |
| row space | 行空间 | 矩阵各行的张成，也就是 $`\mathrm{Col}(A^T)`$ |
| left null space | 左零空间 | $`N(A^T)`$，即满足 $`A^T\mathbf{y}=\mathbf{0}`$ 的向量组成的空间 |
| right-hand side | 右端向量 | $`A\mathbf{x}=\mathbf{b}`$ 中的目标输出 $`\mathbf{b}`$ |
| pivot | 主元 | 阶梯形矩阵中每个非零行的领先非零元素 |
| pivot column | 主元列 | 包含主元、提供独立方向的列 |
| free column | 自由列或非主元列 | 不包含主元的列 |
| pivot variable | 主元变量 | 由方程和自由变量决定的变量 |
| free variable | 自由变量 | 可以独立选取的参数 |
| row echelon form | 行阶梯形 | 主元下方为零的阶梯形矩阵 |
| RREF | 简化行阶梯形 | 主元为 $`1`$，且主元列其余位置全为 $`0`$ |
| rank | 秩 | 主元数量，也是列空间的维数 |
| row rank | 行秩 | 行空间的维数，与列秩相等 |
| null space | 零空间 | 所有满足 $`A\mathbf{x}=\mathbf{0}`$ 的输入组成的空间 |
| nullity | 零度 | 零空间的维数，即自由变量数量 |
| special solution | 特殊解 | 依次把一个自由变量设为 $`1`$、其余设为 $`0`$ 得到的解 |
| particular solution | 特解 | $`A\mathbf{x}=\mathbf{b}`$ 的某一个具体解 $`\mathbf{x}_p`$ |
| complete solution | 通解 | $`\mathbf{x}_p+N(A)`$，即非齐次方程的全部解 |
| affine space | 仿射空间 | 子空间经过平移后得到的集合 |
| affine combination | 仿射组合 | 系数之和为 $`1`$ 的线性形式组合 |
| elimination matrix | 消元矩阵或行变换矩阵 | 把行操作表示成左乘矩阵；合并后满足 $`EA=R`$ |
| full rank | 满秩 | 秩达到 $`\min(m,n)`$ |
| invertible matrix | 可逆矩阵 | 存在逆矩阵 $`A^{-1}`$ 的方阵 |
