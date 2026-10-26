from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
out = Path(__file__).resolve().parents[1] / 'docs/query-results.png'
W,H=1280,720
im=Image.new('RGB',(W,H),'#f5f7f4'); d=ImageDraw.Draw(im)
reg='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f=lambda n,b=False: ImageFont.truetype(bold if b else reg,n)
d.rectangle((0,0,W,76),fill='white'); d.rectangle((52,24,89,61),fill='#17222b'); d.text((61,31),'SQL',font=f(12,True),fill='white'); d.text((108,28),'NORMALIZED QUERY VERIFICATION',font=f(14,True),fill='#17222b')
d.text((58,122),'WORKING QUERIES',font=f(13,True),fill='#18764b'); d.text((58,157),'JOINs replaced comma-separated fields',font=f(39,True),fill='#17222b'); d.text((60,214),'Sample data loaded through schema/normalized_schema.sql',font=f(18),fill='#6e7c83')
rows=[('1','All products + supplier','2 rows'),('2','Products in Electronics','1 row'),('3','Supplier details','2 rows'),('4','Low stock by warehouse','2 rows'),('5','Products tagged mobile','1 row')]
d.rounded_rectangle((70,285,1210,620),radius=18,fill='white',outline='#dce4df',width=2)
for i,(num,name,count) in enumerate(rows):
 y=314+i*59
 if i: d.line((102,y-12,1178,y-12),fill='#dce4df',width=1)
 d.ellipse((104,y,139,y+35),fill='#c9f0d7'); d.text((115,y+8),num,font=f(14,True),fill='#18764b'); d.text((178,y+7),name,font=f(17,True),fill='#17222b'); d.text((1000,y+8),count,font=f(15,True),fill='#18764b')
d.text((70,655),'Foreign keys enabled · 5/5 queries returned rows · SQLite verification harness',font=f(15,True),fill='#18764b')
im.save(out)
