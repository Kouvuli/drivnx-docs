from PIL import Image, ImageDraw, ImageFont
import sys
A='/home/kali/Desktop/Conflux/docs/archive/figures-original/'
OUT=sys.argv[1]
FONTS={'liberation':'/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
       'geist':'/home/kali/Desktop/Conflux/conflux-landing/node_modules/next/dist/compiled/@vercel/og/Geist-Regular.ttf'}
FONT=FONTS[sys.argv[2]]

def clear(im,box,*sample_ys):
    # fill each column with the average of background pixels on clean rows near the area (JPEG noise averages out)
    x0,y0,x1,y1=box; px=im.load()
    for x in range(x0,x1):
        cs=[px[x,y] for y in sample_ys]
        c=tuple(sum(ch)//len(cs) for ch in zip(*cs))
        for y in range(y0,y1): px[x,y]=c

def fit(text,width):
    # font size whose rendered width best matches the original line width
    best=None
    for s10 in range(100,260):
        f=ImageFont.truetype(FONT,s10/10)
        w=f.getlength(text)
        if best is None or abs(w-width)<best[0]: best=(abs(w-width),s10/10)
    return best[1]

def darkest(im,box):
    x0,y0,x1,y1=box; px=im.load()
    return min((px[x,y] for x in range(x0,x1) for y in range(y0,y1)),key=sum)

# ---- Figure 1
im=Image.open(A+'figure1-architecture.jpg').convert('RGB')
ink=darkest(im,(523,665,727,716))
body_size=fit('artifact metadata, and local files',727-523)
sub_size=fit('(SQLite + project files)',710-571)
clear(im,(566,633,766,656),657)
clear(im,(518,660,766,719),658)
d=ImageDraw.Draw(im)
fb=ImageFont.truetype(FONT,body_size); fs=ImageFont.truetype(FONT,sub_size)
# anchor 'ls' = left/baseline; original baselines measured from glyph bounds
d.text((571,648),'(SQLite + artifact files)',font=fs,fill=ink,anchor='ls')
for i,line in enumerate(['Stores project configuration,','artifacts and cached profile results.','Never source data. ADR pending.']):
    d.text((523,677+18*i),line,font=fb,fill=ink,anchor='ls')
    assert 523+fb.getlength(line)<764, line
# legend: drop ", SLAs" by re-assembling original glyph pixels, then re-centre the line
y0,y1=867,889
paren=im.crop((1244,y0,1248,y1))
left=im.crop((1025,y0,1213,y1))           # "e.g., data contract (rules, constraints" (ends before the comma)
clear(im,(1020,y0,1256,y1),862,889,891)
shift=14                                   # keeps the shortened line centred where the old one was
im.paste(left,(1025+shift,y0))
im.paste(paren,(1212+shift,y0))
im.save(OUT+'/figure1-architecture.jpg',quality=95)

# ---- Figure 2: "Data quality checks and monitoring" -> "Data quality checks"
im2=Image.open(A+'figure2-reference-landscape.jpg').convert('RGB')
clear(im2,(958,437,1076,461),435)
im2.save(OUT+'/figure2-reference-landscape.jpg',quality=95)
print('sizes', body_size, sub_size, 'ink', ink)
