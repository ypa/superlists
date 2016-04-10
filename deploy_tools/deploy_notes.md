## Deployment commands

Depending on your PC/laptop environment you might have to do:
```bash
$ ssh-add ~/.ssh/your-ec2-key-pair.pem
```
If you're on a new PC you might have to generate that private key pair file. Notes are on Evernote, search for it in vzmm notebook with tags `deployment`, `tdd`, `tddbook`, `ec2`, `ssh`, etc.

### Pre-check
Make sure you commit all your changes and push it to github.

### staging
```bash
cd ~/work/practice/tdd/superlists/deploy_tools
[ypa@anna deploy_tools]$ fab deploy:host=yan@superlists-staging.wintextiles.com
```

### prod
```bash
cd ~/work/practice/tdd/superlists/deploy_tools
[ypa@anna deploy_tools]$ fab deploy:host=yan@superlists.wintextiles.com
```


