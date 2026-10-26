from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
OUT=Path('video_frames'); OUT.mkdir(exist_ok=True)
W,H=1280,720; bg='#f5f7f4'; ink='#17222b'; muted='#6e7c83'; green='#18764b'; mint='#c9f0d7'; line='#dce4df'; white='#fff'
reg='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f=lambda n,b=False: ImageFont.truetype(bold if b else reg,n)
def base(k,t,s=''):
 im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im); d.rectangle((0,0,W,74),fill=white); d.rectangle((52,24,90,61),fill=ink); d.text((61,31),'3NF',font=f(11,True),fill=white); d.text((110,28),'ECOMMERCE DATABASE REVIEW',font=f(14,True),fill=ink); d.text((58,120),k.upper(),font=f(13,True),fill=green); d.text((58,157),t,font=f(40,True),fill=ink); d.text((60,216),s,font=f(18),fill=muted); return im,d
def save(im,n): im.save(OUT/f'{n:02d}.png')
im,d=base('Challenge 2','From messy rows to 3NF','A normalized e-commerce schema with working product queries.')
d.rounded_rectangle((70,310,1210,585),radius=20,fill=white,outline=line,width=2)
for x,h,b in [(110,'1NF','Atomic values'),(440,'2NF','Full-key facts'),(770,'3NF','No transitive data')]:
 d.ellipse((x,370,x+62,432),fill=mint); d.text((x+18,387),'✓',font=f(28,True),fill=green); d.text((x,465),h,font=f(18,True),fill=ink); d.text((x,503),b,font=f(15),fill=muted)
save(im,1)
im,d=base('The broken baseline','One products row did too much','Categories, tags, supplier fields, and warehouse stock were all packed into one record.')
for y,h,b in [(300,'categories = “Electronics, Mobile”','multi-valued column violates 1NF'),(390,'supplier_name + phone + email','repeated supplier facts cause update anomalies'),(480,'warehouse_location + stock_quantity','inventory is a separate business fact')]:
 d.rounded_rectangle((78,y,1200,y+60),radius=11,fill=white,outline=line,width=2); d.text((105,y+19),h,font=f(16,True),fill=ink); d.text((700,y+19),b,font=f(14),fill=green)
save(im,2)
im,d=base('Normalized model','Each table owns one kind of fact','Relationships are explicit, queryable, and protected by keys.')
di=Image.open('docs/normalized-er.png').convert('RGB'); di.thumbnail((1120,395)); im.paste(di,((W-di.width)//2,270)); save(im,3)
im,d=base('Query migration','JOINs make the relationships visible','The application still gets the same answers, now from consistent source tables.')
for y,h,b in [(305,'CATEGORY FILTER','products → product_categories → categories'),(395,'SUPPLIER DETAILS','products → suppliers'),(485,'LOW STOCK','products → inventory → warehouses')]:
 d.rounded_rectangle((78,y,1200,y+60),radius=11,fill=white,outline=line,width=2); d.text((105,y+19),h,font=f(14,True),fill=green); d.text((390,y+19),b,font=f(17),fill=ink)
save(im,4)
im,d=base('Verification','Five queries still work','The harness loads the schema, enables foreign keys, inserts sample data, and executes the rewritten queries.')
res=Image.open('docs/query-results.png').convert('RGB'); res.thumbnail((1040,330)); im.paste(res,(120,280)); save(im,5)
im,d=base('Trade-off','Clean writes, explicit reads','Normalization adds joins, but removes duplicate values and makes updates reliable.')
d.rounded_rectangle((70,320,1210,560),radius=20,fill=ink)
for i,(a,b) in enumerate([('8 tables','entities, bridges, and inventory facts'),('5 queries','all returned sample rows'),('3NF','maintainability before premature denormalization')]):
 y=360+i*58; d.text((110,y),a,font=f(20,True),fill=mint); d.text((560,y),b,font=f(19),fill=white)
d.text((70,640),'When Clean Design Gets Complex · Challenge 2 · normalized schema submitted for review',font=f(15,True),fill=green); save(im,6)
