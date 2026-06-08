# intro

`SceneSetup.intro();`

# intro-play-button

(...51)

[ΠΑΙΞΕ!](#intro-start) `publish("intro-to-game-1"); Game.OVERRIDE_CHOICE_LINE=true;`

# intro-start

(...500)

`clearText()`

n3: Πριν ξεκινήσουμε, πώς θες *εσύ* να διαβάζεις;

`publish("show_options_bottom")`

# intro-start-2

n3: Τώρα, ας ξεκινήσουμε την ιστορία μας...

```
publish("hide_tabs");
clearText();
```

(...1000)

`publish("intro-to-game-2")`

n2: ΑΥΤΟΣ ΕΙΝΑΙ ΕΝΑΣ ΑΝΘΡΩΠΟΣ

(...600)

`clearText()`

(...300)

`publish("intro-to-game-3")`

# act1

```
SceneSetup.act1();
publish("hide_tabs");
music('battle', {volume:0.5});
```

(...300)

n: ΚΑΙ ΑΥΤΟ ΕΙΝΑΙ ΤΟ ΑΓΧΟΣ ΤΟΥ ΑΝΘΡΩΠΟΥ

n: _ΕΣΥ_ ΕΙΣΑΙ ΤΟ ΑΓΧΟΣ

(#act1_normal)


# act1_normal

```
hong({body:"putaway"});
sfx("rustle");
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Όχι. Όχι, όχι, δεν ακούω. Θα δω το κινητό μου.

```
sfx("rustle2");
hong({body:"phone1", mouth:"neutral", eyes:"neutral"})
```

n: Η ΔΟΥΛΕΙΑ ΣΟΥ ΕΙΝΑΙ ΝΑ ΠΡΟΣΤΑΤΕΥΕΙΣ ΤΟΝ ΑΝΘΡΩΠΟ ΣΟΥ ΑΠΟ *ΚΙΝΔΥΝΟ*

`bb({eyes:"look", mouth:"small_lock", body:"fear"})`

b: Ωχ! Ξοδεύεις τη ζωή σου στο Twitter! Πάλι!

```
bb({eyes:"normal", mouth:"normal", body:"normal"});
hong({eyes:"annoyed"});
```

h: Ναι, απορώ γιατί δεν κάθομαι απλά να ακούω τις σκέψεις μου πιο συχνά.

`hong({eyes:"neutral"});`

n: ΓΡΗΓΟΡΑ, ΠΡΟΕΙΔΟΠΟΙΗΣΕ ΤΟΥΣ ΓΙΑ *ΚΙΝΔΥΝΟ!*

```
bb({eyes:"look"});
```

[Ωχ όχι, κοίτα αυτό το φρικτό νέο!](#act1d_news)

[Ωχ όχι, αυτό το tweet μιλάει κρυφά για *εμάς;*](#act1d_subtweet)

[Έι, ένα GIF με γάτα που πίνει γάλα](#act1d_milk)

# act1d_milk

`hong({mouth:"smile", eyes:"surprise"});`

h: Χεχ ναι είναι χαριτωμένο, εγώ--

```
hong({mouth:"shock", eyes:"shock"});
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.8;
```

b: ΟΙ ΓΑΤΕΣ ΔΕΝ ΧΩΝΕΥΟΥΝ ΤΟ ΓΑΛΑ ΚΑΙ ΕΙΜΑΣΤΕ ΑΠΑΙΣΙΟΙ ΓΙΑΤΙ ΑΠΟΛΑΜΒΑΝΟΥΜΕ ΚΑΚΟΠΟΙΗΣΗ ΖΩΩΝ

(...200)

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
attack("20p", "bad");
publish("hp_show");
```



