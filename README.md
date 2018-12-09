Overview
========

To run simple simulation of 1966 King models: </p>
<i>git clone https://github.com/jleagle94/final_project.git</p>
  cd /final_project/HW40/root/</p>
  Rappture </p>
  </i>
This will automatically run the tool.xml file linked to king_model.py. A window will appear. Play with parameters. Output will be on the RHS of the window as "Result" with three graphs: 1) Density, &rho;, vs. Radius 2) Maximum velocity ("v_max") vs. Radius 3) Gravitational potential energy per unit mass, &psi;, vs. radius.</p>

To run python version: </p>
<i>
  python3 plot_lambda.py 3 rho</p>
  </i>
or</p>
<i>
  python3 plot_lambda.py 4 psi</p>
  </i>
or</p>
<i>
  python3 plot_lambda.py 2 v_max</p>
</i>

Installing Rappture</p>
------------
You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.  Type the following:</p>
* git clone http://github.com/mbradle/astr8300_rappture.git</p>
* cd astr8300_rappture</p>
* rappture</p>

Info: King Models</p>
----
Original work: *http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1966AJ.....71...64K&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf*</p>
<b>Objective:</b> Describe self-gravitating stellar dynamical systems. Generally well-describes globular clusters and elliptical galaxies.</p>
<b>Assumptions:</b> Spherical symmetry. Constant radius. At r=R of sphere, total energy of a star is zero, E=0 - potential for star to escape. Treat stellar distribution as an isothermal gas at a given temperature.</p>
<b>Goals:</b> Surface brightness. Velocity distributions.</p>
<b>Input:</b> Mass density as a function of central gravitational potential. Mass density, &rho;, from King's paper:</p>
**&rho;(&psi;)=exp(w)*scipy.special.erf(sqrt(w))-sqrt((4*w)/(pi))*(1+(2*w)/3)**   #In code, &psi;=w.</p>
Plug into the Poisson equation for the central potential:</p>
**d/dr(r^2*d&psi;/dr)=-4*pi*G*r^2*&rho;(&psi;)**</p>
Use separation of variables to set up two ordinary differential equations to solve simultaneously in rappture for Poisson's equation, finding &psi;:</p>
**Defined as king(x,y) in code**</p>
<b>Output:</b> three graphs based on the above calculations. 1) Density (&rho;) vs. Radius, 2) Potential (&psi;) vs. Radius, 3) Maximum Velocity (v_max) vs. Radius.</p>

To run:</p>
type:</p>
<i>Rappture</i></p>
then hit *Simulate*.</p>

Authors</p>
-------

- Bradley S. Meyer <mbradle@clemson.edu></p>
- Jordan L. Eagle <jeagle@clemson.edu></p>
*ASTR8300 Fall 2018*.
