# Netjets Phenom 300 Mate

## Overview
Training application for Netjets Phenom 300 pilots. Combines system knowledge with procedures.

## Project Structure
- `app.py` - Main Streamlit application
- `assets/hydraulics/` - Screenshots for hydraulic system module
- `assets/electrics/` - Screenshots for electrical system module

## Screenshot Naming Convention
For the Hydraulics module, name files as:
- `hyd_intro.png` - Introduction
- `hyd_schematic.png` - System schematic
- `hyd_panel.png` - Cockpit controls
- `hyd_synoptic.png` - MFD synoptic page
- `hyd_cas.png` - CAS messages
- `hyd_hitemp.png` - High temp procedure
- `hyd_lopres.png` - Low pressure procedure
- `hyd_sov_fail.png` - SOV fail procedure

## Running the App
```
streamlit run app.py --server.port 5000
```
