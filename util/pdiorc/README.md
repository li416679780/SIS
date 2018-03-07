Padding Oracle Attack是针对CBC链接模式的攻击，和具体的加密算法无关，换句话说，这种攻击方式不是对加密算法的攻击，而是针对算法的使用不当进行的攻击。那么padding oracle attack是怎么实现的呢？下面我将详细说一下我的理解。

首先我们了解一下使用CBC模式加密敏感信息的服务器是怎么处理我们提交的内容的。假设我们向服务器提交了正确的密码，我们的密码在经过CBC模式加密后传给了服务器，这时服务器会对我们传来的信息尝试解密，如果可以正常解密会返回一个值表示正确，如果不能正常解密则会返回一个值表示错误。而事实上，判断提交的密文能不能正常解密，第一步就是判断密文最后一组的填充值是否正确，也就是观察最后一组解密得到的结果的最后几位，如果错误将直接返回错误，如果正确，再将解密后的结果与服务器存储的结果比对，判断是不是正确的用户。也就是说服务器一共可能有三种判断结果：

1.密文不能正常解密；

2.密文可以正常解密但解密结果不对；

3.密文可以正常解密并且解密结果比对正确；

其中第一种情况与第二 三种情况的返回值一定不一样，这就给了我们可乘之机——我们可以利用服务器的返回值判断我们提交的内容能不能正常解密，进一步讲，我们可以知道最后一组密文的填充位符不符合填充标准。

[![Padding oracle attack详细解析](http://image.3001.net/images/20171019/15083434757270.png!small)](http://image.3001.net/images/20171019/15083434757270.png)

如上图所示，明文填充了四位时，如果最后一组密文解密后的结果（Intermediary Value也就是中间值）与前一组密文（Initialization Vector也就是IV值）异或得到的最后四位是0×04，那么服务器就会返回可以正常解密。

回忆一下前面我们说过的CBC模式的解密过程，第n组密文解密后的中间值与前一组的密文异或便可得到明文，现在我们不知道解密的密钥key，但我们知道所有的密文，因此只要我们能够得到中间值便可以得到正确的密文（进行一次异或运算便可），而中间值是由服务器解密得到的，因此我们虽然不知道怎么解密但我们可以利用服务器帮我们解密，我们所要做的是能确定我们得到的中间值是正确的，这也是padding oracle attack的核心——找出正确的中间值。

那么我们该如何利用服务器帮我们找到中间值呢？我们刚刚说过，服务器会根据我们提交的密文能否正确解密给我们返回不同的值，这里就有一个可以利用的逻辑判断，判断的标准是最后几位的填充值是否符合标准，再回忆一下前面说的PKCS #5填充和CBC模式的解密过程，我们不难理解下面的攻击过程：

（1）假设我们捕获到了传输的密文并且我们知道是CBC模式采用的什么加密算法，我们把密文按照加密算法的要求分好组，然后对倒数第二组密文进行构造；

（2）先假定明文只填充了一字节，对倒数第二组密文的最后一字节从0×00到0xff逐个赋值并逐个向服务器提交，直到服务返回值表示构造后的密文可以正常解密，这意味着构造后的密文作为中间值（图中黄色的那一行）解密最后一组明文，明文的最后一位是0×01（如图所示），也就是说构造的倒数第二组密文的最后一字节与最后一组密文对应中间值（绿色的那一行）的最后一位相异或的结果是0×01；

[![Padding oracle attack详细解析](http://image.3001.net/images/20171019/15083441758558.png!small)](http://image.3001.net/images/20171019/15083441758558.png)

（3）利用异或运算的性质，我们把我们构造的密文的最后一字节与0×01异或便可得到最后一位密文解密后的中间值是什么，这里我们设为M1，这一过程其实就是对应下图CBC解密过程中红圈圈出来的地方，1就是我们想要得到的中间值，二就是我们构造的密文也就是最后一组密文的IV值，我们已经知道了plaintext的最后一字节是0×01，从图中可以看到它是由我们构造的IV值与中间值的最后一字节异或得到的；

[![Padding oracle attack详细解析](http://image.3001.net/images/20171019/15083453084853.png!small)](http://image.3001.net/images/20171019/15083453084853.png)

（4）再假定明文填充了两字节也就是明文最后两字节是0×02，接着构造倒数第二组密文，我们把M1与0×02异或可以得到填充两字节时密文的最后一位应该是什么，这时候我们只需要对倒数第二位进行不断地赋值尝试（也是从0×00到0xff），当服务器返回值表示可以正常解密时，我们把此时的倒数第二位密文的取值与0×02异或便可得到最后一组密文倒数第二字节对应的中间值；

（5）后再构造出倒数第三倒数第四直到得到最后一组密文的中间值，把这个中间值与截获的密文的倒数第二位异或便可得到最后一组分组的明文；

（6）舍弃掉最后一组密文，只提交第一组到倒数第二组密文，通过构造倒数第三组密文得到倒数第二组密文的铭文，最后我们便可以得到全部的明文