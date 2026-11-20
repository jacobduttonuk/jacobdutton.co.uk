import html
src=open('/home/claude/src/index.src.html').read().replace('__AGENT_MD__',html.escape(open('/home/claude/jacobdutton.co.uk/llms.txt').read().rstrip(),quote=False))
b=open('/home/claude/src/photo.b64').read().strip()
meta='''<link rel="icon" href="/favicon.svg?v=2" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png?v=2" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<link rel="canonical" href="https://www.jacobdutton.co.uk/">
<meta property="og:type" content="profile">
<meta property="og:description" content="I get AI working for large companies, groups and investors: choosing where it pays, proving it works and getting people using it.">
<meta property="og:url" content="https://www.jacobdutton.co.uk/">
<meta property="og:image" content="https://www.jacobdutton.co.uk/jacob-dutton.jpg">
<meta name="twitter:card" content="summary">
'''
import base64,re
IM=['stage-copenhagen-frontier','stage-copenhagen-close','stage-copenhagen-wide']
for n in IM:
    src_a=None
art=src
for n in IM:
    art=art.replace('__IMG_'+n+'__','data:image/jpeg;base64,'+base64.b64encode(open('/home/claude/jacobdutton.co.uk/images/'+n+'.jpg','rb').read()).decode())
art=art.replace('__PHOTO__','data:image/jpeg;base64,'+b).replace('href="/llms.txt"','href="https://www.jacobdutton.co.uk/llms.txt" target="_blank" rel="noopener"')
open('/home/claude/src/index.html','w').write(art)
ff='<style>@font-face{font-family:"Space Grotesk";src:url(spacegrotesk.woff2) format("woff2");font-weight:300 700}</style>'
open('/home/claude/src/preview.html','w').write(art.replace('<style>',ff+'<style>',1))
live=re.sub(r'__IMG_([a-z-]+)__',r'/images/\1.jpg',src).replace('__PHOTO__','/jacob-dutton.jpg').replace('<link rel="preconnect" href="https://fonts.googleapis.com">',meta+'<link rel="preconnect" href="https://fonts.googleapis.com">',1)
open('/home/claude/jacobdutton.co.uk/index.html','w').write(live)
print('built', len(art), len(live))
