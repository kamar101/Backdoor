<h1>Backdoor - Maintaining Access</h1>

<h2>Description</h2>
The project consists of two python script that runs in a command and control model. The backdoor.py script would hypothetically be installed on a target computer after gaining access. The server.py script will be on the attackers' computer listening for a connection request from the target IP address. The connection request will be sent after running the backdoor.py script on the victim's computer. Once a connection is established, the attacker will be able to run basic shell commands on the victim's computer. 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>Windows 11 (Attacker)</b>
- <b>Linux (Target)</b>

<h2>Program walk-through:</h2>

<p>
Run the server.py script on the attack computer: python3 server.py <br/>
<img src="https://imgur.com/B8J9JVI.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Run the backdoor.py script on the target computer: python3 backdoor.py  <br/>
<img src="https://imgur.com/obI0Mls.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Verify a connection has been established on the attackers' computer<br/>
<img src="https://imgur.com/iwhnppj.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Run basic command from the attacker's computer<br/>
<img src="https://imgur.com/EeSL0yH.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
