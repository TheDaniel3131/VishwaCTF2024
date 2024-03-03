For this challenge, you basically have to go to the required deployed site: https://ch661857156535.ch.eng.run/ (need to enable website deployment)

Follow the click here, it shows the error/go back page right. But if you look closely in inspect element, it tells us to change user agent to
IITAIN. Because I am a noob, so I just google how to change user agent and I found this useful website :)

https://www.searchenginejournal.com/change-user-agent/368448/

and after following it and entering the 'IITAIN' user-agent, it will redirect me to this page: https://ch661857156535.ch.eng.run/auth-iit-user.php and I just use the classic SQL injection payload to bypass the vulnerable login: https://github.com/payloadbox/sql-injection-payload-list.

and you will find the flag after you did that. 
https://ch661857156535.ch.eng.run/home.php

you can check all the pictures in the imgur link caused I just do a quick writeup lol.
https://imgur.com/a/0iFMwg8


SOME OTHER USEFUL LINKS DURING MY RESEARCH:
https://d00mfist.gitbooks.io/ctf/content/web-scanning.html



