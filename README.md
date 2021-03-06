.. M0IXP-RC

: M0IXP_RC Rotator Controller :
===============================

M0IXP-RC is designed to be a simple GUI based Antenna Rotator Controller using python3. 

M0IXP_RC will connect to any GS232 enabled rotator controller. providing a simple config 
and control interface. 

: Features :
============

It will add 2 new features that most other open source controllers seem to lack. 

1)  The ability to provide a background image to be displayed behind the compass image. 
    This will allow a circle map centered at the QTH to be displayed. Opacity and colour 
    options will also be available to the configuration interface. This will all be 
    provided using the cartopy library included within most python releases.
    
2)  A field to supply a 4 or 6 digit maidenhead grid locator for the destination. This 
    will be used with the config supplied QTH locator to discover a required angle then 
    direct the antenna towards it. This will need to be built such that cartopy.crs 
    points are translatable to and from the center of Maidenhead grid locators.

: Other possible options :
==========================

*   the ability receive or request callsign from log files with directional data or grid 
    locations and automatically rotate to that location.

*   adding the ability to provide a map real diameter within configuration and have the 
    code zoom in or out and place markers to indicate maidenhead grid locations or 
    direction and distance data over the map as data is passed into the software. 
