Battery - RimWorld Wiki
 
 
- 
- 
 
 

- 

- 
- 
- 
- 
- 
- 
- 
- 
 

 
 

 
 

 

 Battery

 
 From RimWorld Wiki

 (Redirected from Batteries)

 

 
 

 Jump to navigation
 Jump to search
 
 Battery

Stores electricity for later use. Charged batteries explode when exposed to rain or fire.

Base Stats

Type
Building&#32;–&#32; Power

Market Value
200&#160; [Note]

Mass
20 kg

Beauty
-15

HP
100

Flammability
100%

Path Cost
50 (21%)

Building

Size
1&#160;&#215;&#160;2

Minifiable
True

Placeable
True

Passability
pass through only

Cover Effectiveness
40%

 
Blocks Wind
True

Terrain Affordance
Medium

Efficiency
50%

Creation

Required Research
Battery

Work To Make
800&#160;ticks (13.33&#160;secs)

Resources to make
 70 + 2

Deconstruct yield
 35 + 1

Destroy yield
 17 - 18 + 0 - 1

 Technical
 
thingCategories
BuildingsPower 
 

The battery is a building that stores excess power from a grid to use when needed.

Contents

- 1 Acquisition

- 2 Summary

- 2.1 Health

- 3 Analysis

- 3.1 Power storage

- 3.2 Efficiency

- 4 Version history

Acquisition[edit]

Batteries can be constructed once the Battery research project has been completed. Each requires &#160;70&#160;Steel, &#160;2&#160;Components and 800&#160;ticks (13.33&#160;secs) of work modified by the construction speed of the builder. 
Batteries can not be bought from traders.

Summary[edit]

 
Batteries connect directly to the wind turbine and the attached coolers, with no conduits. This power grid will only "Zzztt" if the batteries get rained on.

Batteries automatically charge from the excess power in a power grid and discharge to power other buildings connected to the grid when there is a power deficit. However, batteries have a 50% efficiency, meaning they take in only half of a grid's excess power. For example, an excess of 200 W for 24 hours will only store 100 Wd. Power is evenly divided between all batteries connected to the grid in question. Each battery is initially constructed empty but can store up to 600 Wd (Watt-days) of power at once. 1 Watt-day is equal to powering a 1 W appliance for 24 hours. There is no need to enable or "switch" to battery power - a charged battery will automatically discharge as soon as there is a power deficit in the grid to which it is connected. There is no limit or penalty for power output.

Each tile of battery will also transfer an infinite amount of power through it, as if it were a power conduit. Therefore, electric appliances like standing lamps can connect within 6 tiles of a battery. The battery can't connect in the same way; it requires an adjacent conduit, battery, or power generator to power. A wire will appear when a valid connection is made; you may need to use the Reconnect gizmo on the appliance for it to be powered.

Batteries lose 5 Wd of stored power per day, even if they aren't connected to anything or are uninstalled in their minified state. Batteries can't be turned off, but a power switch can disconnect them from other buildings. 

Batteries are temporarily disabled by sources of EMP, with downtime scaling to the EMP damage dealt.[Verify] During this time, it will not provide any power. Unlike mechanoids, batteries do not adapt to EMP and thus can be continuously restunned.

Health[edit]

An installed battery will short circuit if left in the rain or snow without a roof. In addition, the total power stored in batteries contributes the effect of any short circuit that affects that power grid.

Like other furniture, batteries are not subject to deterioration, but short-circuits from rain or snow cause damage.[Verify/Detail] Their health does not impact power storage, discharge, or any other function. Temperature also has no effect past fire creation. However, batteries can explode when reaching low enough health.[Detail]

Analysis[edit]

Batteries are most useful when using wind turbines or solar panels, both of which are highly variable power sources. Using a battery creates a 'cushion' in case no power is generated, thus making their power more reliable. Batteries are required to use any sort of solar power at night or during an eclipse. Fueled generators can also benefit, as excess power can be stored and remain usable after the generator is turned off.

Even in colonies that do not use wind or solar energy, batteries are useful to cover spikes in power usage, such as short-circuits, turret arrays, or electric smelters. A battery can cover arbitrarily high power needs, for a length of time dependent on the sudden power requirement. As an example, an array of 20 mini-turrets and 4 autocannon turrets draws 3200 W of power. Instead of building another geothermal generator, each battery will power this for more than 4 in-game hours.

Uninstalled batteries can be used whenever power needs to be transported. They can be used to power remote deep drills, or even be put on a caravan. This allows for electric appliances like mini-turrets to be used far away from your base.

As there is no limit on charge or discharge rate and power is divided evenly between batteries, the minimum number of batteries should be used to achieve the required storage. For every 600Wd is routinely left unfilled that is an additional 5W spent, components consumed by breakdowns, and &#160;70&#160;Steel, &#160;2&#160;Components spent all for no benefit.

Power storage[edit]

Separating your batteries behind stone walls will help keep potential fires from spreading. As you'll rarely need to access the battery itself, stone doors can be safely used for "battery rooms". You may want to keep some additional batteries behind a power switch on a separate network, so they can be brought online in the case of a "Zzzt..." event. Alternatively, you can uninstall batteries and keep them in a warehouse. Either way, the discharge is negligible.

When powering an emergency array, the battery group should be isolated. There should be 1 power switch to the main power grid, which should be turned on or off when needed. This keeps power safe from a short circuit. When powering a security array, you can place another, separate switch connected to your turrets to easily power them on or off. 

Unused electric work benches and powered appliances can be turned off to reduce total power usage, via the Designate toggle power order in the work bench menu. This requires a pawn to travel to the appliance and manually turn it off or on. A faster alternative to the Designate Toggle Power order is to build a single piece of power conduit unattached to any power source near the work bench. The Reconnect order from the work bench menu will instantly toggle power connection between the unpowered, solo conduit and your main power grid, saving power usage without requiring work or travel from your pawns.

Efficiency[edit]

When calculating power capacity, keep in mind that charge efficiency is only 50%; half of the excess energy is lost. This is particularly relevant when planning a sun lamp setup. The lamp draws 2900 W during the day, and 0 W during the night, for an average demand of 1595 W. However, an average power of 1595 W is not sufficient, and only enough to power the lamp for 6 hours. Simply adding more batteries will not change this; the problem is the lack of energy. In this scenario, adding another solar generator would be enough to power the lamp.

Version history[edit]

- 0.0.245 - Charged batteries now explode while burning.

Architect

Power
Power conduit (Hidden, Waterproof) &#8226; Power switch &#8226; Wood-fired generator &#8226; Chemfuel powered generator &#8226; Wind turbine
(research)
Battery &#8226; Geothermal generator &#8226; Solar generator &#8226; Watermill generator &#8226; Toxifier generator &#8226; Bioferrite generator &#8226; Gravcore power cell
(uncraftable)
Vanometric power cell &#8226; Unstable power cell 
Related
Ship reactor &#8226; Electroharvester

 
 

 

Retrieved from "https://rimworldwiki.com/index.php?title=Battery&oldid=175815"

 Category: - Power

Hidden categories: - Unverified articles
- Pages that need fact checking

 

 Navigation menu

 
 

 
 Personal tools
 

 
 
 
 - Not logged in
- Talk
- Contributions
- Create account
- Log in

 
 

 
 

 
 Namespaces
 

 
 
 
 - Page
- Discussion

 
 

 

 
 
 Variants
 

 
 
 
 
 
 

 

 
 

 
 Views
 

 
 
 
 - Read
- Edit
- View history

 
 

 

 
 
 More
 

 
 
 
 
 
 

 
 
 Search
 

 
 
 
 
 
 
 

 

 

 

 

 
 
 

 

 
 RimWorld
 

 
 
 
 - Official Site
- Official Twitter
- Subreddit
- Community Discord

 
 

 

 
 Navigation
 

 
 
 
 - Main page
- Recent changes
- Random page

 
 

 

 
 Tools
 

 
 
 
 - What links here
- Related changes
- Special pages
- Printable version
- Permanent link
- Page information
- Browse properties

 
 

 

 
 - This page was last edited on 24 February 2026, at 13:02.

 - Content is available under CC BY-SA 3.0 unless otherwise noted.

 
 
 - Privacy policy

 - About RimWorld Wiki

 - Disclaimers

 
 
 - 

 -