# Torque & Code

Our team for the **2026 NASA Space Apps Challenge**, Eindhoven local event (virtual), 14–15 November 2026.

Mechanical + computer science students building a **Lunar Landing Site Navigator**: a tool that compares landing sites and dates at the Moon's south pole by sunlight (power) and Earth visibility (direct-to-Earth comms).

**Team website:** https://kapnistos.github.io/torque-and-code/

## Links

| What | Link |
|---|---|
| Team website | https://kapnistos.github.io/torque-and-code/ |
| GitHub repo | https://github.com/kapnistos/torque-and-code |
| WhatsApp: Eindhoven event | _to add (shared after registering)_ |
| WhatsApp: our team | _to add_ |
| Space Apps team page | _to add (after the team is created)_ |
| Eindhoven local event | https://www.spaceappschallenge.org/2026/local-events/eindhoven/ |
| Space Apps 2026 | https://www.spaceappschallenge.org/2026/ |
| All challenges | https://www.spaceappschallenge.org/2026/challenges/ |
| Find a team | https://www.spaceappschallenge.org/2026/find-a-team/ |
| JPL Horizons (web) | https://ssd.jpl.nasa.gov/horizons/ |
| JPL Horizons API docs | https://ssd-api.jpl.nasa.gov/doc/horizons.html |

## Team

| Name | Study | Role |
|---|---|---|
| _to add_ | | Physics & power model |
| _to add_ | | Data & ephemeris (JPL Horizons) |
| _to add_ | | Front end & charts |
| _to add_ | | Scoring, demo & submission |

## The challenge

Missions to the lunar south pole face hard limits on light and communication: the Sun stays near the horizon and Earth can drop out of view. The tool should let planners, teachers and the public compare sites and dates quickly.

Pipeline:

1. Pick candidate sites (lat/lon) and a date range
2. Query JPL Horizons for Sun and Earth azimuth/elevation from each site
3. Power model: `P = A · η · 1361 W/m² · sin(e_sun)`, plus battery sizing for the longest dark gap
4. Comms windows: hours with Earth above the horizon
5. Score and compare sites side by side

## Before Saturday

- [ ] Everyone creates a Space Apps account and registers for 2026
- [ ] Everyone picks **Eindhoven** as local event
- [ ] Team owner creates "Torque & Code" and picks the challenge
- [ ] Everyone joins the team and the WhatsApp group
- [ ] Everyone accepts the GitHub invite
- [ ] Test one Horizons query for a south-pole site

## Repo layout

```
site/page.html   website source (edit this)
build.py         wraps site/page.html into index.html for GitHub Pages
index.html       generated: do not edit by hand
```

Edit `site/page.html`, run `python build.py`, commit both files.

_Participant team project. Not affiliated with or endorsed by NASA._
