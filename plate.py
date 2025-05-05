import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

fig, ax = plt.subplots(figsize=(10,6))
ax.axis('off')

def box(x,y,text,w=2.4,h=0.9):
    ax.add_patch(Rectangle((x,y),w,h,fill=False,linewidth=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=10)

# Latent variables and parameters
box(1,4.2,"$\\tau$")
box(4,4.2,"$z^{\\mathrm{raw}}_i$")
box(7,4.2,"$z_i = \\dfrac{z^{\\mathrm{raw}}_i}{\\sqrt{\\tau}}$",w=3.5)

box(0.2,2.4,"$\\beta_{\\mathrm{lights}}=1$")
box(3,2.4,"$\\beta_{\\mathrm{NDVI}}$")
box(6,2.4,"$\\beta_{\\mathrm{roads}}$")

box(0.2,1.0,"$\\sigma_{\\mathrm{lights}}$")
box(3,1.0,"$\\sigma_{\\mathrm{NDVI}}$")
box(6,1.0,"$\\sigma_{\\mathrm{roads}}$")

box(9,2.2,"$x_{i,k}$",w=2.0,h=1.2)

def arrow(x1,y1,x2,y2):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),
                arrowprops=dict(arrowstyle="->",lw=1.2))

arrow(3.4,4.65,7,4.65)     # tau -> z
arrow(5.9,4.65,7,4.65)     # z_raw -> z
arrow(8.8,3.0,9.0,2.8)     # z -> x

arrow(2.6,2.85,9,2.85)
arrow(5.4,2.85,9,2.85)
arrow(8.2,2.85,9,2.85)

arrow(2.6,1.5,9.2,2.5)
arrow(5.4,1.5,9.2,2.5)
arrow(8.2,1.5,9.2,2.5)

# Plates
ax.add_patch(Rectangle((0,0.4),11.4,4.4,fill=False,linewidth=1.8))
ax.text(11.2,4.55,"for each cell $i$",ha='right',fontsize=10)
ax.text(10,3.7,"for each proxy $k$",ha='center',fontsize=10)

plt.tight_layout()

# Save 
out_path = Path("plate.png")
fig.savefig(out_path,dpi=150,bbox_inches='tight')
out_path