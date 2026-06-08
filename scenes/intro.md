# intro

`SceneSetup.intro();`

# intro-play-button

(...51)

```
_.PLAYED_BEFORE = !!window.localStorage.continueChapter;
```

{{if !_.PLAYED_BEFORE}}
`Game.OVERRIDE_FONT_SIZE=30;`
{{/if}}

{{if !_.PLAYED_BEFORE}}
[#play1# ΠΑΙΞΕ! #play2#](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="act2"}}
[_ΣΥΝΕΧΕΙΑ_: Το Πάρτι](#act2) `publish("LOAD_GAME", ["act2"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="act3"}}
[_ΣΥΝΕΧΕΙΑ_: Το Άλλο Πάρτι](#act3) `publish("LOAD_GAME", ["act3"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="act4"}}
[_ΣΥΝΕΧΕΙΑ_: Το Άλλο Σάντουιτς](#act4) `publish("LOAD_GAME", ["act4"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="replay"}}
`Game.OVERRIDE_FONT_SIZE=30;`
{{/if}}

{{if _.PLAYED_BEFORE && window.localStorage.continueChapter=="replay"}}
[#play1# ΞΑΝΑΠΑΙΞΕ! #play2#](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if _.PLAYED_BEFORE}}
[Επιλογή Κεφαλαίου](#chapter-select) `Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

[(σημειώσεις περιεχομένου)](#intro-play-button) `Game.OVERRIDE_CHOICE_LINE=true; publish('show_cn');`

# chapter-select

`publish("HACK_chselect");`

[I. Το Σάντουιτς](#intro-start) `publish("HACK_chselect_end"); publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`

[II. Το Πάρτι](#act2) `publish("HACK_chselect_end"); publish("LOAD_GAME", ["act2"]); Game.OVERRIDE_CHOICE_LINE=true;`

{{if window.localStorage.act3}}
[III. Το Άλλο Πάρτι](#act3) `publish("HACK_chselect_end"); publish("LOAD_GAME", ["act3"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if !window.localStorage.act3}}
[III. The Other Party]()
{{/if}}

{{if window.localStorage.act4}}
[IV. Το Άλλο Σάντουιτς](#act4) `publish("HACK_chselect_end"); publish("LOAD_GAME", ["act4"]); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if !window.localStorage.act4}}
[III. The Other Sandwich]()
{{/if}}

{{if window.localStorage.credits}}
[V. Τίτλοι](#to-credits) `publish("HACK_chselect_end"); Game.OVERRIDE_CHOICE_LINE=true;`
{{/if}}

{{if !window.localStorage.credits}}
[V. Credits]()
{{/if}}

[(κύριο μενού)](#intro-play-button) `publish("HACK_chselect_end"); Game.OVERRIDE_CHOICE_LINE=true;`

# to-credits

`stopAllSounds();`

(...101)

(#credits)

# intro-start

(...500)

`clearText()`

n3: Καλώς ήρθες! Αυτό είναι λιγότερο «παιχνίδι» και περισσότερο διαδραστική ιστορία. Ελπίζω σου αρέσει να διαβάζεις, μαλάκα!

n3: Πριν ξεκινήσουμε, πώς θες *εσύ* να διαβάζεις;

`publish("show_options_bottom")`

# intro-start-2

n3: Τέλεια! Σημείωση: μπορείς πάντα να αλλάξεις τις ρυθμίσεις με το εικονίδιο ⚙ κάτω. Επίσης, το παιχνίδι αποθηκεύεται αυτόματα σε κάθε κεφάλαιο!

n3: Τώρα, ας ξεκινήσουμε την ιστορία μας...

`clearText()`

(...1000)

`publish("intro-to-game-2")`

n2: ΑΥΤΟΣ ΕΙΝΑΙ ΕΝΑΣ ΑΝΘΡΩΠΟΣ

(...600)

`clearText()`

(...300)

`publish("intro-to-game-3")`
