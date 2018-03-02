From Freebuff2012

**1.MS12-020 Microsoft Remote Desktop Use-After-Free DoS (CVE-2012-0002, MSB-MS12-020):**
MS12-020是一个高危远程代码执行漏洞，可以通过向远程桌面端口发送特定的RDP包获得管理员权限。

**2.Microsoft Server Service Relative Path Stack Corruption (CVE-2008-4250, MSB-MS08-067):** 一个流行了四年的经典漏洞了，可以稳定利用Windows 2003 Server和Windows XP，经久不衰。

**3.Microsoft Server Service NetpwPathCanonicalize Overflow (CVE-2006-3439, MSB-MS06-040):** 一个六年的漏洞可以利用没有打官方补丁的Windows NT 4.0。如果你需要一个NT机器的远程root，这个module可能会是你的第一选择。

**4.Microsoft RPC DCOM Interface Overflow (CVE-2003-0352, MSB-MS03-026):** Microsoft RPC接口远程溢出缺陷允许执行任意代码,也是一个骨灰级漏洞。

**5.Microsoft Windows 7 / Server 2008 R2 SMB Client Infinite Loop (CVE-2010-0017, MSB-MS10-006):** 我们并不确定为什么这个module这么火，这个漏洞需要攻击者将特制的 SMB 响应发送到客户端发起的 SMB 请求，此漏洞可能允许远程执行代码。 要利用这些漏洞，攻击者必须诱使用户建立与恶意 SMB 服务器的 SMB 连接。

**6.Adobe PDF Embedded EXE Social Engineering (CVE-2010-1240):** 这种 AdobeReader类型的漏洞不用多说，可以用来嵌入并执行Meterpreter，并使用比如社工的方法来利用。

**7.Apache mod_isapi <= 2.2.14 Dangling Pointer (CVE-2010-0425):** Apache HTTP Server 早于2.3.7版本的2.3.x系列核心mod_isapi模块modules/arch/win32/mod_isapi.c存在安全漏洞，如果远程用户向Apache服务器的mod_isapi模块发送了特制的请求之后又发送了重置报文，就可能导致从内存中卸载目标ISAPI模块

**8.Java AtomicReferenceArray Type Violation Vulnerability (CVE-2012-0507):** 这个一开始被发现为java 0day。详情可查看http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

**9.Microsoft Windows Authenticated User Code Execution (CVE-1999-0504):** 传说中的PSExec模块，熟悉msf的朋友都应该很清楚，hash传递等教科书般的方法就不多说了。

**10.Microsoft Plug and Play Service Overflow (CVE-2005-1983, MSB-MS05-039):** MS05-039是一个远程执行代码和本地特权提升漏洞，在 Windows 2000 上，匿名攻击者可能试图远程利用此漏洞。相信很多朋友都用ms05039做过反弹:)