Overview
========

To run simple simulation of 1966 King models go to https://github.com/jleagle94/final_project/HW40/root/
type <i>
  Rappture 
  </i>
This will automatically run the tool.xml file linked to king_model.py. A window will appear. Play with parameters. Output will be on the RHS of the window as "Result" with three graphs: 1) Density vs. Radius 2) Maximum velocity ("v_max") vs. Radius 3) Gravitational potential energy per unit mass (psi) vs. radius.

To run python version: 
<i>
  python3 plot_lambda.py 3 rho
  </i>
or
<i>
  python3 plot_lambda.py 4 psi
  </i>
or
<i>
  python3 plot_lambda.py 2 v_max
</i>

Installing Rappture
------------
You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.  Type the following:
* git clone http://github.com/mbradle/astr8300_rappture.git
* cd astr8300_rappture
* rappture

Info: King Models
----
Original work: *http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1966AJ.....71...64K&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf*
<b>Objective:</b> Describe self-gravitating stellar dynamical systems. Generally well-describes globular clusters and elliptical galaxies.
<b>Assumptions:</b> Spherical symmetry. Constant radius. At r=R of sphere, total energy of a star is zero, E=0 - potential for star to escape. Treat stellar distribution as an isothermal gas at a given temperature.
<b>Goals:</b> Surface brightness. Velocity distributions as stars interact.
<b>Input:</b> mass density as a function of central gravitational potential.
Mass density, &rho; from King's paper:
**&rho;(&psi;)=exp(w)*scipy.special.erf(sqrt(w))-sqrt((4*w)/(pi))*(1+(2*w)/3)** #In code, &psi;=w.
Plug into the Poisson equation for the central potential:
**d/dr(r^2*d&psi;/dr)=-4*pi*G*r^2*&rho;(&psi;)**
Use separation of variables to set up two ordinary differential equations to solve simultaneously in rappture for Poisson's equation, finding &psi;:
**Defined as king(x,y) in code**
<b>Output:</b> three graphs based on the above calculations. 1) Density (&rho;) vs. Radius, 2) Potential (&psi;) vs. Radius, 3) Maximum Velocity (v_max) vs. Radius.

To run:
type:
*Rappture*
then hit *Simulate*.

Authors
-------

- Bradley S. Meyer <mbradle@clemson.edu>
- Jordan L. Eagle <jeagle@clemson.edu></p>
*ASTR8300 Fall 2018*.
