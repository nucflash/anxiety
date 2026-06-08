# act1

```
SceneSetup.act1();
```

(...300)

n: ΚΑΙ ΑΥΤΟ ΕΙΝΑΙ ΤΟ ΆΓΧΟΣ ΤΟΥ ΑΝΘΡΩΠΟΥ

n: _ΕΣΥ_ ΕΙΣΑΙ ΤΟ ΆΓΧΟΣ

{{if window.localStorage.continueChapter=="replay"}}
(#act1_replay)
{{/if}}

{{if window.localStorage.continueChapter!="replay"}}
(#act1_normal)
{{/if}}



# act1_replay

`hong({mouth:"0_neutral", eyes:"0_neutral"})`

h: Ω, γεια! Πάλι εδώ;

`hong({eyes:"0_neutral"})`

n: Η ΔΟΥΛΕΙΑ ΣΟΥ ΕΙΝΑΙ ΝΑ ΠΡΟΣΤΑΤΕΥΕΙΣ ΤΟΝ ΑΝΘΡΩΠΟ ΣΟΥ ΑΠΟ *ΚΙΝΔΥΝΟ*

`bb({eyes:"look", mouth:"small_lock"})`

n: ΜΑΛΙΣΤΑ, ΤΟ ΝΑ ΞΑΝΑΠΑΙΖΕΙΣ ΑΥΤΟ ΤΟ ΠΑΙΧΝΙΔΙ ΤΟΥΣ ΒΑΖΕΙ ΣΕ *ΚΙΝΔΥΝΟ* ΤΩΡΑ

n: ΓΡΗΓΟΡΑ, ΠΡΟΕΙΔΟΠΟΙΗΣΕ ΤΟΥΣ!

```
sfx("squeak");
bb({body:"squeeze_talk"});
hong({body:"0_squeeze"});
```

b: Άνθρωπο! Άκου, κινδυνεύουμε! Ο παίκτης...

[...θα μας βασανίσει ξανά!](#act1_replay_torture)

[...δεν θα βρει εναλλακτικό τέλος!](#act1_replay_alternate)

[...θα πάθει ludonarrative dissonance!](#act1_replay_dissonance)

# act1_replay_torture

```
window.HACK_REPLAY = JSON.parse(localStorage.act4);
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

{{if window.HACK_REPLAY.act1_ending=="fight"}}
b: Θα μας κάνουν να μαζευτούμε σαν μπάλα και να κλάψουμε!
{{/if}}

{{if window.HACK_REPLAY.act1_ending=="flight"}}
b: Θα μας κάνουν να σκοτώσουμε το τηλέφωνό σου επειδή σου έδωσε κρίση πανικού!
{{/if}}

{{if window.HACK_REPLAY.a2_ending=="fight"}}
b: Θα μας κάνουν να *ΜΗΝ* χτυπήσουμε τον οικοδεσπότη του πάρτι!
{{/if}}

{{if window.HACK_REPLAY.a2_ending=="flight"}}
b: Θα μας κάνουν να χτυπήσουμε τον Συμπαθητικό Anti-Villain οικοδεσπότη του πάρτι!
{{/if}}

{{if window.HACK_REPLAY.a3_ending=="jump"}}
h: Λοιπόν, τουλάχιστον ίσως δεν πηδήξουμε από τη σκεπή αυτή τη φο--
{{/if}}

{{if window.HACK_REPLAY.a3_ending=="walkaway"}}
b: ΘΑ ΜΑΣ ΚΑΝΟΥΝ ΝΑ ΠΗΔΗΞΟΥΜΕ ΑΠΟ ΤΗ ΣΚΕΠΗ.
{{/if}}

`bb({body:"fear"});`

b: ΟΛΑ ΑΥΤΑ ΤΑ ΝΕΑ ΤΡΟΜΕΡΑ ΠΡΑΓΜΑΤΑ ΘΑ ΜΑΣ ΣΥΜΒΟΥΝ, ΚΑΙ ΜΕΤΑ ΘΑ--

(#act1_replay_end)


#act1_replay_alternate

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

h: Ναι, η ιστορία *συνολικά* είναι ίδια, αλλά κάθε κεφάλαιο έχει δύο πιθανά τέλη, συν όλες τις διακλαδώσεις διαλόγου επιλο--

`bb({body:"fear"});`

b: Ο παίκτης θα απογοητευτεί, θα κλείσει αυτό το tab, θα σβήσει το λογισμικό μας, και μετά θα--

(#act1_replay_end)


# act1_replay_dissonance

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich"});
```

h: Λιούντ-τι τώρα;

`bb({eyes:"normal"});`

b: Η ιστορία ήταν για το πώς μπορείς να *ΕΠΙΛΕΞΕΙΣ* να χτίσεις μια υγιή συνεργασία με τον φόβο σου,

`bb({eyes:"normal_right"});`

b: Αλλά το να ξαναπαίζεις το παιχνίδι δίνει την ίδια ιστορία, υπονοώντας ότι οι *ΕΠΙΛΟΓΕΣ* σου δεν έχουν σημασία,

`bb({eyes:"narrow_eyebrow"});`

b: Έτσι δείχνοντας αντίφαση ανάμεσα στο μήνυμα του παιχνιδιού και τη μηχανική του,

`bb({eyes:"fear"});`

b: Έτσι ξετυλίγοντας το ύφασμα αυτού του αφηγηματικού σύμπαντος,

`bb({body:"fear"});`

b: Και μετά θα--

(#act1_replay_end)


# act1_replay_end

`bb({body:"panic"})`

b: ΘΑ ΠΕΘΑΝΟΥΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜ

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.clearText();
```

(...1001)

```
bb({body:"laugh"});
hong({body:"laugh"});
Game.clearText();
sfx("laugh");
```

(...5001)

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({body:"0_sammich"});
```

h: Εντάξει, ας ξαναμπώ στον ρόλο.

```
Game.clearText();
```

n4: (ΑΦΗΣΕ ΤΟ _ΔΙΚΟ ΣΟΥ_ ΆΓΧΟΣ ΜΠΛΑ ΜΠΛΑ ΜΠΛΑ Ο,ΤΙ ΜΟΙΑΖΕΙ ΠΕΡΙΣΣΟΤΕΡΟ ΜΕ ΤΟΝ _ΔΙΚΟ ΣΟΥ_ ΦΟΒΟ ΜΠΛΑ ΜΠΛΑ ΞΕΡΕΙΣ ΤΗ ΔΙΑΔΙΚΑΣΙΑ)

```
sfx("squeak");
hong({body:"0_squeeze"});
bb({body:"squeeze"});
```

(#act1_normal_choice)



# act1_normal

`hong({mouth:"0_neutral", eyes:"0_annoyed"})`

h: Α, καλά, ο λύκος μου γύρισε. Φααααανταστικά.

`hong({eyes:"0_neutral"})`

n: Η ΔΟΥΛΕΙΑ ΣΟΥ ΕΙΝΑΙ ΝΑ ΠΡΟΣΤΑΤΕΥΕΙΣ ΤΟΝ ΑΝΘΡΩΠΟ ΣΟΥ ΑΠΟ *ΚΙΝΔΥΝΟ*

`bb({eyes:"look", mouth:"small_lock"})`

n: ΜΑΛΙΣΤΑ, ΑΥΤΟ ΤΟ ΣΑΝΤΟΥΙΤΣ ΤΟΥΣ ΒΑΖΕΙ ΣΕ *ΚΙΝΔΥΝΟ* ΤΩΡΑ

n: ΓΡΗΓΟΡΑ, ΠΡΟΕΙΔΟΠΟΙΗΣΕ ΤΟΥΣ!

```
sfx("squeak");
bb({body:"squeeze_talk"});
hong({body:"0_squeeze"});
```

b: Άνθρωπο! Άκου, κινδυνεύουμε! Ο κίνδυνος είναι...

`bb({body:"squeeze"})`

n4: (ΑΦΗΣΕ ΤΟ _ΔΙΚΟ ΣΟΥ_ ΆΓΧΟΣ ΝΑ ΒΓΕΙ ΝΑ ΠΑΙΞΕΙ! ΔΙΑΛΕΞΕ Ο,ΤΙ ΜΟΙΑΖΕΙ ΠΕΡΙΣΣΟΤΕΡΟ ΜΕ ΑΥΤΟ ΠΟΥ ΣΟΥ ΛΕΕΙ Ο _ΔΙΚΟΣ ΣΟΥ_ ΦΟΒΟΣ)

(#act1_normal_choice)

# act1_normal_choice

[Τρώμε μόνοι μας το μεσημεριανό! Πάλι!](#act1a_alone) `bb({body:"squeeze_talk"})`

[Δεν είμαστε παραγωγικοί όσο τρώμε!](#act1a_productive) `bb({body:"squeeze_talk"})`

[Το λευκό ψωμί είναι κακό για μας!](#act1a_bread) `bb({body:"squeeze_talk"})`

# act1a_alone

```
bb({body:"normal", mouth:"small", eyes:"narrow"});
hong({body:"0_sammich"});
```

b: Δεν ξέρεις ότι η μοναξιά συνδέεται με πρόωρο θάνατο όσο και 15 τσιγάρα την ημέρα;-

`Game.OVERRIDE_TEXT_SPEED = 2;`

`bb({mouth:"normal", eyes:"normal_right"})`

b: (Holt-Lunstad 2010, PLoS Medicine)

`hong({eyes:"0_annoyed"})`

h: Ε, ευχαριστώ που παραθέτεις πηγές αλλά--

`Game.OVERRIDE_TEXT_SPEED = 2;`

`bb({body:"fear", mouth:"normal", eyes:"fear"})`

b: Άρα αν δεν βγούμε με κάποιον *τώρα αμέσως* θα--

`bb({body:"panic"})`

b: ΘΑ ΠΕΘΑΝΟΥΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜ

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "alone");
publish("hp_show");
```

(...2500)

`_.fifteencigs = true`

n: ΧΡΗΣΙΜΟΠΟΙΗΣΕΣ *ΦΟΒΟ ΜΗ ΑΓΑΠΗΜΕΝΟΥ*

(#act1b)

# act1a_productive

```
bb({body:"normal", mouth:"small", eyes:"normal"});
hong({body:"0_sammich"});
```

b: Βγάλε το laptop και δούλεψε τώρα αμέσως!

`hong({eyes:"0_annoyed"})`

h: Ε, προτιμώ να μη βάλω ψίχουλα στο πληκτρολόγι--

```
bb({mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Αν δεν συνεισφέρουμε στο σώμα της κοινωνίας, είμαστε παράσιτο της κοινωνίας!

b: Το σώμα-κοινωνία θα πάει στον γιατρό-κοινωνία για φάρμακα να σκοτώσει τα παράσιτα-κοινωνίας και μετά θα--

```
bb({body:"panic", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: ΘΑ ΠΕΘΑΝΟΥΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜ

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "bad");
publish("hp_show");
```

(...2500)

`_.parasite = true`

n: ΧΡΗΣΙΜΟΠΟΙΗΣΕΣ *ΦΟΒΟ ΚΑΚΟΥ ΑΝΘΡΩΠΟΥ*

(#act1b)

# act1a_bread

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({body:"0_sammich", eyes:"0_annoyed"});
```

h: Έχουν αναπαραχθεί αυτές οι μελέτες--

```
bb({body:"fear", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Το επεξεργασμένο σιτάρι θα ανεβάσει τη γλυκόζη μας κι έτσι θα μας κόψουν όλα τα άκρα και μετά θα--

`bb({body:"panic"})`

b: ΘΑ ΠΕΘΑΝΟΥΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜΜ

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"0_shock", eyes:"0_shock"});
attack("18p", "harm");
publish("hp_show");
```

(...2500)

`_.whitebread = true`

n: ΧΡΗΣΙΜΟΠΟΙΗΣΕΣ *ΦΟΒΟ ΒΛΑΒΗΣ*

(#act1b)

# act1b

n: ΕΙΝΑΙ ΥΠΕΡΑΠΟΤΕΛΕΣΜΑΤΙΚΟ

`bb({mouth:"smile", eyes:"smile"});`

b: Βλέπεις, άνθρωπο; Είμαι ο πιστός σου λύκος-φύλακας!

`bb({body:"pride_talk"});`

b: Πίστεψε το ένστικτό σου! Τα συναισθήματά σου είναι πάντα έγκυρα!

`bb({body:"pride"});`

n: ΦΕΡΕ ΤΗ ΜΠΑΡΑ ΕΝΕΡΓΕΙΑΣ ΤΟΥ ΑΝΘΡΩΠΟΥ ΣΟΥ ΣΤΟ ΜΗΔΕΝ

n: ΓΙΑ ΝΑ ΠΡΟΣΤΑΤΕΥΣΕΙΣ ΤΙΣ ΦΥΣΙΚΕΣ + ΚΟΙΝΩΝΙΚΕΣ + ΗΘΙΚΕΣ ΤΟΥ ΑΝΑΓΚΕΣ, ΜΠΟΡΕΙΣ ΝΑ ΧΡΗΣΙΜΟΠΟΙΗΣΕΙΣ:

n: ΦΟΒΟ *ΒΛΑΒΗΣ* #harm#

n: ΦΟΒΟ *ΜΗ ΑΓΑΠΗΜΕΝΟΥ* #alone#

n: ΚΑΙ ΦΟΒΟ *ΚΑΚΟΥ ΑΝΘΡΩΠΟΥ* #bad#

`Game.OVERRIDE_TEXT_SPEED = 1.25;`

n4: (PRO-TIP: ΠΑΙΞΕ ΤΙΣ ΕΠΙΛΟΓΕΣ ΠΟΥ ΧΤΥΠΑΝΕ ΤΟΥΣ ΠΙΟ ΒΑΘΙΑ, ΣΚΟΤΕΙΝΑ ΦΟΒΑ ΣΟΥ!~)

h: ...

```
hong({body:"putaway"});
sfx("rustle");
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

(...1000)

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

h: ξέρεις τι, ίσως ήρθε η ώρα να δω το τηλέφωνό μου.

```
sfx("rustle2");
hong({body:"phone1", mouth:"neutral", eyes:"neutral"})
```

n: ΠΡΟΣΤΑΤΕΥΣΕ ΤΟΝ ΑΝΘΡΩΠΟ ΣΟΥ

n: ΑΠΟ ΤΟΝ ΚΟΣΜΟ. ΑΠΟ ΑΛΛΟΥΣ ΑΝΘΡΩΠΟΥΣ. ΑΠΟ ΤΟΝ ΕΑΥΤΟ ΤΟΥ.

n: ΚΑΛΗ ΤΥΧΗ

(...500)

`Game.clearText()`

(...500)

(#act1c)

# act1c

`music('battle', {volume:0.5})`

n: ΓΥΡΟΣ ΕΝΑ: *ΜΑΧΗ!*

`bb({body:"normal", mouth:"normal", eyes:"normal"});`

h: Χμ. Το Facebook λέει ότι γίνεται πάρτι αυτό το Σαββατοκύριακο.

`bb({eyes:"uncertain"});`

b: Δεν κάνει αυτός ο περίεργος πάρτι *κάθε* Σαββατοκύριακο;

`bb({eyes:"uncertain_right"});`

b: Τι εσωτερικό κενό προσπαθούν να γεμίσουν; Πρέπει να είναι χάλια μέσα τους!

`hong({eyes:"surprise"});`

h: Επίσης, πήρα πρόσκληση;

`bb({eyes:"fear", mouth:"normal"});`

b: Λοιπόν!

[Πες ναι, αλλιώς θα πεθάνουμε από μοναξιά!](#act1c_loner)

[Πες όχι, είναι γεμάτο δηλητηριώδη ναρκωτικά!](#act1c_drugs)

[Αγνόησέ το, απλώς κάνουμε τα πάρτι λυπηρά.](#act1c_sad)

# act1c_loner

{{if _.fifteencigs}}
b: Δεκαπέντε τσιγάρα την ημέρα, άνθρωπο! Δεκαπέντε!
{{/if}}

{{if !_.fifteencigs}}
`Game.OVERRIDE_TEXT_SPEED = 1.5;`
{{/if}}

{{if !_.fifteencigs}}
b: Μετά κανείς δεν θα έρθει στο κηδειόφορό μας, θα ρίξουν τη στάχτη μας στη θάλασσα, θα μας φάει μια φάλαινα,
{{/if}}

{{if !_.fifteencigs}}
b: και θα γίνουμε ΚΟΠΡΑΝΑ ΦΑΛΑΙΝΑΣ!
{{/if}}

{{if !_.fifteencigs}} `_.whalepoop = true` {{/if}}

(...500)

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`bb({eyes:"normal"});`

{{if !_.fifteencigs}}
b: Οπότε ναι, πρέπει να πάμε σε εκείνο το πάρτι!
{{/if}}

{{if _.parasite}}
b: Απλώς πάρε το laptop να δουλέψουμε, και να μην είμαστε παράσιτο της κοινωνίας.
{{/if}}

{{if _.whitebread}}
b: Μόνο να μη σερβίρουν ΛΕΥΚΟ ΨΩΜΙ
{{/if}}

`hong({mouth:"anger", eyes:"anger"});`

h: ΘΕΕ. Αν θα σε κάνω να σωπάσεις, εντάξει.

h: Θα πω ναι.

{{if _.whalepoop}}
b: Κόπρανα φάλαινας, άνθρωπο! Κόπρανα φάλαινας!
{{/if}}

`_.partyinvite="yes"`

(#act1d)

# act1c_drugs

`bb({mouth:"small", eyes:"fear"});`

{{if _.whitebread}}
b: ή ακόμα χειρότερα... ΛΕΥΚΟ ΨΩΜΙ
{{/if}}

{{if _.whitebread}}
`Game.OVERRIDE_TEXT_SPEED = 1.5;`
{{/if}}

{{if _.whitebread}}
b: Θα κάνουμε υπερβολική δόση σε τόσο μεθ και λευκό ψωμί που δεν θα χωρέσει το χοντρό πτώμα μας στον κρεματοριο!
{{/if}}

{{if !_.whitebread}}
b: Θα κάνουμε υπερβολική δόση σε τόσα ναρκωτικά που ο νεκροθάφτης θα αναρωτηθεί πώς το σώμα μας ήταν *ήδη* εμβαλαμένο!
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

{{if _.parasite}}
b: Εξάλλου, δεν μπορούμε να πάρτι, πρέπει να δουλέψουμε αλλιώς είμαστε τρομερό παράσιτο της κοινωνίας!
{{/if}}

`hong({mouth:"anger", eyes:"anger"});`

h: ΘΕΕ. Αν θα σε κάνω να σωπάσεις, εντάξει.

h: Θα πω όχι.

`_.partyinvite="no"`

(#act1d)

# act1c_sad

`bb({eyes:"uncertain_right", mouth:"normal"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

{{if _.fifteencigs}}
b: Το μόνο που κάνουμε ποτέ είναι να κλαίμε σε μια γωνιά για το πόσο θανατηφόρα είναι η μοναξιά όσο 15 τσιγάρα την ημέρα.
{{/if}}

{{if _.parasite}}
b: Το μόνο που κάνουμε ποτέ στα πάρτι είναι να ανησυχούμε ότι πρέπει να είμαστε παραγωγικοί.
{{/if}}

{{if _.whitebread}}
b: Το μόνο που κάνουμε ποτέ είναι να ανησυχούμε ότι οι ανθυγιεινές επιλογές φαγητού θα μας σκοτώσουν.
{{/if}}

```
bb({mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"lookaway"});
```

h: ααα, αναρωτιέμαι γιατί.

`hong({eyes:"neutral"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

b: Οπότε αν πάμε θα τους κάνουμε να νιώσουν άσχημα, αλλά αν απορρίψουμε την πρόσκληση θα τους κάνουμε κι αυτό να νιώσουν άσχημα!

`bb({body:"fear", eyes:"fear"});`

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

b: ΟΛΑ ΤΑ ΚΑΝΟΥΜΕ ΕΙΝΑΙ ΝΑ ΚΑΝΟΥΜΕ ΤΟΥΣ ΑΝΘΡΩΠΟΥΣ ΝΑ ΝΙΩΘΟΥΝ ΑΣΧΗΜΑ, ΟΠΟΤΕ ΠΡΕΠΕΙ ΝΑ ΝΙΩΘΟΥΜΕ ΑΣΧΗΜΑ

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

`hong({mouth:"anger", eyes:"anger"});`

h: Φου. Αν θα σε κάνω να σωπάσεις, εντάξει.

h: Θα αγνοήσω την πρόσκληση.

`_.partyinvite="ignore"`

(#act1d)

# act1d

```
bb({body:"normal", mouth:"normal", eyes:"normal"});
hong({mouth:"neutral", eyes:"annoyed"});
```

h: Τέλος πάντων. Το Facebook είναι πολλά. Χρειάζομαι κάτι πιο ήρεμο, λιγότερο άγχος-παραγωγό.

`hong({eyes:"neutral"});`

h: Τι νέο στο Twitter;

`bb({eyes:"look"});`

[Ωχ όχι, κοίτα αυτό το φρικτό νέο!](#act1d_news)

[Ωχ όχι, αυτό το tweet είναι κρυφά για *εμάς;*](#act1d_subtweet)

[Χε, ένα GIF με γάτα που πίνει γάλα](#act1d_milk)


# act1d_news

```
bb({eyes:"pained1"});
music(null, {fade:2});
```

b: Θεέ, νιώθω σαν να καίγεται ο κόσμος, έτσι δεν είναι;

```
bb({eyes:"pained2"});
hong({mouth:"sad", eyes:"sad"});
```

b: Νιώθω σαν να τελειώνει όλα, σαν να πεθαίνει τα πάντα και είμαστε καταδικασμένοι και δεν μπορούμε να κάνουμε τίποτα.

```
Game.OVERRIDE_TEXT_SPEED = 0.5;
bb({mouth:"shut"});
```

b: ...

`bb({mouth:"smile", eyes:"smile"});`

b: Ας κάνουμε retweet αυτό το νέο!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

`_.badnews=true`

```
music('battle', {volume:0.5});
hong({mouth:"anger", eyes:"anger"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Εντάξει θα κάνω retweet απλώς σώπασε παρακαλώ!

`hong({mouth:"neutral", eyes:"annoyed"});`

h: Στο διάολο, ας δούμε το Snapchat.

(#act1e)


# act1d_subtweet

`bb({eyes:"fear"});`

b: Είναι subtweet! Ένα ύπουλο, ύπουλο subtweet!

`hong({eyes:"annoyed"});`

h: Μάλλον όχι;

`bb({eyes:"narrow", mouth:"small"});`

b: αλλά τι γίνεται αν μας κουβεντιάζουν πίσω από την πλάτη μας

h: Δεν μ--

`bb({body:"fear", eyes:"fear", mouth:"normal"});`

b: ΜΠΡΟΣΤΑ ΑΠΟ ΤΗΝ ΠΛΑΤΗ ΜΑΣ

`hong({eyes:"sad", mouth:"sad"});`

h: Δε θ--

`bb({eyes:"narrow", mouth:"small"});`

b: αλλά *τι γίνεται αν*

h: Σ--

`bb({eyes:"narrow_eyebrow"});`

b: *τι γίνεται αν*

```
Game.OVERRIDE_TEXT_SPEED = 0.5;
hong({mouth:"shut"});
```

h: ...

(...1000)

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`_.subtweet=true`

```
hong({mouth:"anger", eyes:"annoyed"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: ε-ΝΤΑΞΕΙ, θα δοκιμάσω Snapchat.

(#act1e)

# act1d_milk

`hong({mouth:"smile", eyes:"neutral"});`

h: Χε ναι αυτό είναι χαριτωμένο, μόλις το έκανα retweet, νομί--

```
hong({mouth:"shock", eyes:"shock"});
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.8;
```

b: ΟΙ ΓΑΤΕΣ ΔΕΝ ΧΩΝΕΥΟΥΝ ΓΑΛΑ ΚΑΙ ΕΙΜΑΣΤΕ ΤΡΟΜΕΡΟΙ ΑΝΘΡΩΠΟΙ ΓΙΑΤΙ ΑΠΟΛΑΜΒΑΝΟΥΜΕ ΚΑΚΟΠΟΙΗΣΗ ΖΩΩΝ

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
attack("18p", "bad");
```

(...2500)


`_.catmilk=true`

```
hong({mouth:"anger", eyes:"annoyed"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: ε-ΝΤΑΞΕΙ, θα δοκιμάσω Snapchat.

(#act1e)

# act1e

`hong({mouth:"neutral", eyes:"neutral"});`

h: Χμ, φωτογραφίες από χθες το βράδυ. Άρα *έτσι* είναι τα εβδομαδιαία πάρτι.

{{if _.partyinvite=="yes"}} (#act1e_said_yes) {{/if}}

{{if _.partyinvite=="no"}} (#act1e_said_no) {{/if}}

{{if _.partyinvite=="ignore"}} (#act1e_said_ignore) {{/if}}

# act1e_said_yes

`hong({mouth:"sad", eyes:"annoyed"});`

h: Ουφ, φαίνεται πολύ γεμάτο για το άγχος μου.

h: Ίσως δεν έπρεπε να είχα πει ναι στην πρόσκληση;

```
hong({mouth:"neutral", eyes:"neutral"});
bb({mouth:"normal", eyes:"normal"});
```

[Να αλλάξουμε την απάντηση; Σαν μαλάκας;](#act1e_yes_dontchange)

[Να αλλάξουμε την απάντηση! Είναι πολύ γεμάτο!](#act1e_yes_changetono)

{{if _.subtweet}}
[Ναι μας έκαναν σίγουρα subtweet.](#act1e_ignore_subtweet)
{{/if}}

{{if _.badnews}}
[Περίμενε, κάναμε retweet χωρίς fact-checking.](#act1e_ignore_factcheck)
{{/if}}

{{if (!_.subtweet && !_.badnews)}}
[Ξέρεις, έχεις πολύ κακή στάση σώματος;](#act1e_ignore_posture)
{{/if}}

# act1e_yes_dontchange

```
bb({eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Μετρούσαν ότι θα έρθουμε και τώρα προδίδουμε την εμπιστοσύνη τους; Θέλεις να πεθάνεις μόνος;

{{if _.fifteencigs}}
b: ΔΕΚΑΠΕΝΤΕ. ΤΣΙΓΑΡΑ.
{{/if}}

{{if _.whalepoop}}
b: ΚΟΠΡΑΝΑ. ΦΑΛΑΙΝΑΣ.
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

```
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Σώπα σώπα θα το κρατήσω ως ναι!

(#act1f)

# act1e_yes_changetono

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Δεν ξέρεις για τις ανθρώπινες ποδοπατήσεις;

```
bb({body:"fear", mouth:"small", eyes:"narrow"});
hong({eyes:"sad", mouth:"sad"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Το 2003 ένα νυχτερινό κέντρο στη Rhode Island είχε φωτιά και ο πανικός έκανε τους ανθρώπους να μπλοκάρουν τις εξόδους κι έτσι 100 άνθρωποι κάηκαν ζωντανοί-

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
hong({mouth:"shock"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: ΘΕΛΕΙΣ ΝΑ ΜΑΣ ΣΥΜΒΕΙ ΑΥΤΟ-

```
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 2.5;
```

b: ΠΕΣ ΟΧΙ ΠΕΣ ΟΧΙ ΠΕΣ ΟΧΙ ΠΕΣ ΟΧΙ ΠΕΣ ΟΧΙ ΠΕΣ ΟΧΙ ΠΕΣ ΟΧΙ ΠΕΣ Ο--


```
bb({body:"normal", eyes:"fear", mouth:"normal"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

```
hong({eyes:"anger", mouth:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Σώπα σώπα θα αλλάξω την απάντηση σε όχι! Θεέ!

(#act1f)

# act1e_said_no

`hong({mouth:"sad", eyes:"sad"});`

h: Χμ... φαίνεται πολύ διασκεδαστικό.

h: Ίσως δεν έπρεπε να είχα πει όχι στην πρόσκληση;

`bb({mouth:"normal", eyes:"normal"});`

[Να αλλάξουμε την απάντηση; Σαν μαλάκας;](#act1e_no_dontchange)

[Να αλλάξουμε την απάντηση! Μην πεθάνεις μόνος!](#act1e_no_changetoyes)

{{if _.subtweet}}
[Ναι μας έκαναν σίγουρα subtweet.](#act1e_ignore_subtweet)
{{/if}}

{{if _.badnews}}
[Περίμενε, κάναμε retweet χωρίς fact-checking.](#act1e_ignore_factcheck)
{{/if}}

{{if (!_.subtweet && !_.badnews)}}
[Ξέρεις, έχεις πολύ κακή στάση σώματος;](#act1e_ignore_posture)
{{/if}}

# act1e_no_dontchange

`bb({eyes:"anger"})`

b: Όλοι μετρούσαν πάνω μας!

b: ...να τους αφήσουμε ήσυχους και να έχουν ωραίο πάρτι χωρίς έναν απαίσιο αηδιαστικό {{if _.whitebread}}τρώγοντα-λευκό-ψωμί{{/if}} creep σαν εμ--


```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

```
bb({body:"normal", eyes:"uncertain", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Σώπα σώπα θα το κρατήσω ως όχι!

(#act1f)

# act1e_no_changetoyes

```
bb({body:"fear", eyes:"fear", mouth:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Η χρόνια μοναξιά αυξάνει τα επίπεδα κορτιζόλης μας καθώς και τον κίνδυνο καρδιαγγειακών νοσημάτων και εγκεφαλικού!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

{{if _.fifteencigs}}
b: ΔΕΚΑΠΕΝΤΕ. ΤΣΙΓΑΡΑ.
{{/if}}

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Σώπα σώπα θα αλλάξω την απάντηση σε ναι! Θεέ!

(#act1f)

# act1e_ignore_subtweet

```
bb({eyes:"fear", mouth:"small"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Όλα τα προβληματικά μας tweets γύρισαν να μας βρουν!

```
bb({body:"fear", eyes:"fear", mouth:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.7;
```

b: Θα μας εκθέσουν και θα μας cancelάρουν και θα μας σύρουν με σκοινί σε άλογο στην υπερ-αυτοκινητόδρομο πληροφοριών!

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Γιατί είσαι έτσι;

(#act1f)

# act1e_ignore_factcheck

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Διαδίδουμε παραπληροφόρηση! Καταστρέφουμε την εμπιστοσύνη στον ελεύθερο Τύπο!

```
bb({body:"scream"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Είμαστε ο λόγος που ο φασισμός θα αναδυθεί από τα ερείπια της δημοκρατίας!

```
bb({body:"normal", eyes:"anger"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

```
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
_.factcheck = true;
```

h: Γιατί είσαι έτσι;

(#act1f)

# act1e_ignore_posture

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Θέλεις να έχεις σπονδυλική στήλη σαν πρέτζελ; Σταμάτα να σκύβεις πάνω στην οθόνη!

```
bb({body:"meta"});
```

b: Αυτό σημαίνει κι εσύ.

```
bb({body:"normal", mouth:"normal"});
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({mouth:"anger", eyes:"anger"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

h: Γιατί είσαι έτσι;

(#act1f)

# act1e_said_ignore

`hong({mouth:"sad", eyes:"sad"});`

h: Χμ... φαίνεται πολύ διασκεδαστικό.

h: Ίσως δεν έπρεπε να είχα αγνοήσει την πρόσκληση;

`bb({mouth:"normal", eyes:"normal"});`

[Συνέχισε να αγνοείς, είμαστε ακόμα party poopers.](#act1e_ignore_continue)

[Όντως, πες ναι.](#act1e_ignore_changetoyes)

[Όντως, πες όχι.](#act1e_ignore_changetono)

# act1e_ignore_continue

`hong({eyes:"annoyed"});`

h: Είναι λίγο αγενές να τους αγνοείς συνέχεια όμως, έτσι δεν είναι;

`bb({eyes:"normal_right"});`

b: Λοιπόν οι άλλοι πάντα αγνοούν *εμάς*, οπότε

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`bb({eyes:"normal"});`

b: ας το κάνουμε κουβάρι.

(#act1f)

# act1e_ignore_changetoyes

`hong({eyes:"surprise", mouth:"smile"});`

h: Μου... αφήνεις να διασκεδάσω;

b: Λοιπόν, εννοώ, η μοναξιά *μπορεί* να μας σκοτώσει.

`hong({eyes:"neutral", mouth:"neutral"});`

(#act1e_no_changetoyes)

# act1e_ignore_changetono

`bb({eyes:"narrow"});`

b: Είναι πολύ γεμάτο. Τα πλήθη είναι επικίνδυνα.

(#act1e_yes_changetono)


# act1f

```
hong({mouth:"neutral", eyes:"neutral"});
bb({body:"normal", mouth:"normal", eyes:"normal"});
```

h: Ό,τι νά 'ναι. Νέα ειδοποίηση Tinder.

`bb({eyes:"uncertain"})`

b: Τι, αυτή η εφαρμογή για one-night stands;

`hong({eyes:"annoyed"})`

h: Δεν είναι εφαρμογή για one-night stands, είναι απλώς τρόπος να γνωρίσεις νέους ανθρώπ--

`bb({eyes:"narrow"})`

b: Είναι εφαρμογή για one-night stands.

```
hong({eyes:"surprise", mouth:"smile"});
bb({eyes:"normal"});
```

h: Ω, έκανα match! Φαίνονται χαριτωμένοι!

```
bb({eyes:"narrow_eyebrow"});
hong({eyes:"sad", mouth:"anger"})
```

h: Μην το χαλάσεις για μέ--

```
bb({body:"panic"});
Game.OVERRIDE_TEXT_SPEED = 2.0;
```

b: ΚΙΝΔΥΝΟΣ ΚΙΝΔΥΝΟΣ ΚΙΝΔΥΝΟΣ ΚΙΝΔΥΝΟΣ ΚΙΝΔΥΝΟΣ ΚΙΝΔΥΝΟΣ

`bb({body:"fear", eyes:"fear", mouth:"normal"})`

[Μας *χρησιμοποιούν* άλλοι άνθρωποι.](#act1f_used_by_others)

[Απλώς *χρησιμοποιούμε* άλλους ανθρώπους.](#act1f_using_others)

[ΤΟ MATCH ΣΟΥ ΕΙΝΑΙ ΣΕΡΙΑΛ ΚΙΛΕΡ](#act1f_killer)

# act1f_used_by_others

`bb({body:"point_crotch", eyes:"normal", mouth:"normal"})`

b: Τα τυχαία one-night stands ίσως γεμίσουν την τρύπα εκεί κάτω,

b: αλλά δεν μπορούν ποτέ να γεμίσουν την τρύπα...

`bb({body:"point_heart", eyes:"pretty", mouth:"small"})`

b: *εδώ* μέσα.

(...1000)

```
bb({body:"normal", mouth:"normal", eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Το θέμα είναι ΘΑ ΠΕΘΑΝΟΥΜΕ ΜΟΝΟΙ

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "alone");
```

(...2500)

`_.hookuphole=true`

(#act1g)

# act1f_using_others

`bb({eyes:"narrow", mouth:"small"})`

b: Νομίζεις ότι τα γεννητικά όργανα άλλων είναι Pokémon για να τα μαζεύουμε;

```
bb({body:"sing", eyes:"pretty", mouth:"shut"});
music("pokemon");
Game.clearText();
Game.FORCE_CANT_SKIP = true;
```

```
Game.FORCE_TEXT_DURATION = 1000;
Game.FORCE_NO_VOICE = true;
```

b: ♫ (pokemon theme song)-

(...5600)

```
bb({mouth:"normal"});
Game.FORCE_TEXT_DURATION = 2400;
```

b: ♫ Θέλω να γίνω, η πιο ^καμμένη^-

(...500)

```
bb({eyes:"narrow", mouth:"small"});
Game.FORCE_TEXT_DURATION = 2100;
```

b: ♫ Σαν κανείς ποτέ δεν ήταν-

(...1500)

```
bb({eyes:"pretty"});
Game.FORCE_TEXT_DURATION = 2300;
```

b: ♫ Μηροί κ' ^κώλοι^, στήθος πληθωρικό-

(...500)

```
bb({eyes:"fear", mouth:"normal"});
Game.FORCE_TEXT_DURATION = 2000;
```

b: ♫ με ^dick^ και balls ιδρωμένα!-

(...1000)

```
bb({eyes:"smile", mouth:"smile"});
Game.FORCE_TEXT_DURATION = 1000;
```

b: ♫ ΠΕΡΒΥ-MON! ΠΡΕΠΕΙ ΝΑ ΤΑ--

```
Game.FORCE_CANT_SKIP = false;
Game.clearText();
music(false);
bb({body:"normal", mouth:"normal", eyes:"normal"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Το θέμα είναι ότι είμαστε χειριστικό creep.

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "bad");
```

(...2500)

`_.pokemon=true`

(#act1g)

# act1f_killer

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

{{if _.whitebread}}
b: Θα σε παγιδεύσουν σε ένα πηγάδι και θα σου ταΐζουν λευκό ψωμί να σε παχύνουν για να φορέσουν το δέρμα σου σαν κοστούμι!
{{/if}}

{{if _.parasite}}
b: Θα σε κοπανήσουν με χρονόμετρο pomodoro και θα πουν «ΕΠΡΕΠΕ ΝΑ ΗΣΟΥΝ ΠΙΟ ΠΑΡΑΓΩΓΙΚΟΣ ΠΑΡΑΣΙΤΟ»
{{/if}}

{{if !_.whitebread && !_.parasite}}
b: Θα σκίσουν τη σάρκα σου σε αιματηρά κομφετί, θα κάνουν τα σπλάχνα σου κορδέλες, και θα ανακατέψουν το αίμα σου σε μπολ με punch!
{{/if}}

{{if !_.whitebread && !_.parasite}}
b: Πώς σου φαίνεται αυτό για πρόσκληση σε πάρτι;
{{/if}}

```
hong({mouth:"shock", eyes:"shock"});
attack("18p", "harm");
```

(...2500)

`_.serialkiller=true`

(#act1g)

# act1g

```
bb({body:"normal", mouth:"normal", eyes:"look"});
hong({body:"2_tired"});
Game.OVERRIDE_TEXT_SPEED = 0.5;
music(false);
```

h: ...

(...500)

h: βαρέθηκα αυτό το παιχνίδι.

(...700)

`Game.OVERRIDE_TEXT_SPEED = 1.5;`

h:
{{if _.fifteencigs}}"loneliness will kill us"... {{/if}}
{{if _.parasite}}"we're a society-parasite"... {{/if}}
{{if _.whitebread}}"don't eat that, it'll kill us"... {{/if}}
{{if _.subtweet}}"they're talking behind our back"... {{/if}}
{{if _.badnews}}"the world is burning"... {{/if}}
{{if _.hookuphole}}"we'll die alone"... {{/if}}
{{if _.serialkiller}}"they're a serial killer"... {{/if}}
{{if _.catmilk}}"cats can't digest milk"... {{/if}}
{{if _.pokemon}}a ^crappy^ parody song... {{/if}}

h: απλώς θέλω να ζήσω τη ζωή μου.

h: απλώς θέλω να είμαι ελεύθερος από όλο αυτό... τον πόνο.

`bb({eyes:"look_sad"});`

b: Χέι... άνθρωπο...

`Game.OVERRIDE_TEXT_SPEED = 0.5;`

b: Θα πάει καλά.

(...600)

`bb({body:"point_heart", eyes:"look_sad_smile", mouth:"smile"});`

b: Ως ο πιστός σου λύκος-φύλακας, θα κρατάω πάντα τα μάτια μου ανοιχτά για κίνδυνο, και θα κάνω ό,τι μπορώ να σε κρατήσω ασφαλή.

`bb({body:"normal", eyes:"look_sad", mouth:"smile"});`

b: Το υπόσχομαι.

(...600)

```
bb({body:"normal", eyes:"normal", mouth:"normal"});
hong({body:"phone1", eyes:"neutral", mouth:"neutral"});
```

h: Τελευταία εφαρμογή. Instagram. Τι έχεις;

`hong({eyes:"sad"});`

h: Είναι... περισσότερες φωτογραφίες από πάρτι.

`hong({mouth:"sad"});`

h: Όλοι φαίνονται τόσο χαρούμενοι. Ελεύθεροι από ανησυχίες. Ελεύθεροι από άγχος.

`hong({mouth:"anger"});`

h: Θεέ, γιατί δεν μπορώ να είμαι σαν αυτούς; Γιατί δεν μπορώ απλώς να είμαι *κανονικός;*

`bb({eyes:"normal_right"});`

b: Μιλώντας για πάρτι, για την πρόσκληση αυτού του Σαββατοκύριακου. Η ΤΕΛΙΚΗ μου απόφαση:

`bb({eyes:"normal"});`

[Πρέπει να πάμε.](#act1g_go) `Game.OVERRIDE_CHOICE_LINE=true`

[Δεν πρέπει να πάμε.](#act1g_dont) `Game.OVERRIDE_CHOICE_LINE=true`

# act1g_go

`_.act1g = "go"`

(#act1h)

# act1g_dont

`_.act1g = "dont"`

(#act1h)

# act1h

b: Πρέπει ν--

```
bb({eyes:"wat", mouth:"small"});
hong({body:"2_fuck"});
```

h: *^ΓΑΜΩΤΟ^.*

`hong({body:"2_you"});`

h: ΕΣΥ.

(...500)

b: τ

(...1500)

`bb({eyes:"wat_2"});`

b: τι;

`hong({body:"phone1", eyes:"anger", mouth:"anger"});`

h: Θα πω ΝΑΙ σε εκείνο το πάρτι,

{{if _.act1g=="go"}}
h: ΟΧΙ επειδή θέλεις εσύ, αλλά επειδή θέλω *εγώ*.
{{/if}}

{{if _.act1g=="dont"}}
h: Ακριβώς ΕΠΕΙΔΗ δεν θέλεις εσύ.
{{/if}}

```
hong({body:"putaway"});
sfx("rustle");
```

h: ΔΕΝ ελέγχεις εμένα.

```
sfx("rustle2");
hong({body:"0_sammich", eyes:"0_annoyed", mouth:"0_neutral"});
```

h: Τώρα συγχώρησέ με ενώ τρώω αυτό το νόστιμο σάντουιτς με ^γαμημένη^ ησυχία.

`hong({body:"2_sammich_eat"});`

(...601)

```
sfx("sandwich");
hong({body:"2_sammich_eaten", eyes:"0_lookaway", mouth:"0_chew1"})
```

(...601)

```
bb({body:"normal", eyes:"uncertain", mouth:"shut"});
Game.OVERRIDE_TEXT_SPEED = 0.5;
```

b: ...

```
bb({eyes:"normal_right"});
Game.OVERRIDE_TEXT_SPEED = 1;
```

b: ...

```
bb({eyes:"fear"});
Game.OVERRIDE_TEXT_SPEED = 4;
```

b: ..................

(...500)

`bb({mouth:"normal"});`

[ΑΑΑΑΑ ΘΑ ΠΕΘΑΝΟΥΜΕ](#act1h_death) `Game.OVERRIDE_CHOICE_LINE = true;`

[ΑΑΑΑΑ ΜΑΣ ΜΙΣΟΥΝ ΟΛΟΙ](#act1h_loneliness) `Game.OVERRIDE_CHOICE_LINE = true;`

[ΑΑΑΑΑ ΕΙΜΑΣΤΕ ΤΡΟΜΕΡΟΙ ΑΝΘΡΩΠΟΙ](#act1h_worthless) `Game.OVERRIDE_CHOICE_LINE = true;`

# act1h_death

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: ΑΑΑΑΑ ΘΑ ΠΕΘΑΝΟΥΜΕ ΑΑΑΑΑΑΑΑΑΑ

```
hong({body:"3_defeated1"});
attack("100p", "harm");
```

(...2500)

(#act1i)

# act1h_loneliness

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: ΑΑΑΑΑ ΜΑΣ ΜΙΣΟΥΝ ΟΛΟΙ ΑΑΑΑΑΑΑΑΑΑ

```
hong({body:"3_defeated1"});
attack("100p", "alone");
```

(...2500)

(#act1i)

# act1h_worthless

```
bb({body:"fear"});
Game.OVERRIDE_TEXT_SPEED = 3;
```

b: ΑΑΑΑΑ ΕΙΜΑΣΤΕ ΤΡΟΜΕΡΟΙ ΑΝΘΡΩΠΟΙ ΑΑΑΑΑΑΑΑΑΑ

```
hong({body:"3_defeated1"});
attack("100p", "bad");
```

(...2500)

(#act1i)

# act1i

```
bb({mouth:"smile_lock", eyes:"smile", body:"normal"});
music('battle', {volume:0.5});
```

n: ΣΥΓΧΑΡΗΤΗΡΙΑ

(...500)

n: ΠΡΟΣΤΑΤΕΥΣΕΣ ΕΠΙΤΥΧΩΣ ΤΙΣ ΦΥΣΙΚΕΣ + ΚΟΙΝΩΝΙΚΕΣ + ΗΘΙΚΕΣ ΑΝΑΓΚΕΣ ΤΟΥ ΑΝΘΡΩΠΟΥ ΣΟΥ

n: ΚΟΙΤΑ ΠΩΣ ΕΙΝΑΙ ΕΥΓΝΩΜΟΝΕΣ!

(...500)

n: ΤΩΡΑ ΠΟΥ Η ΕΝΕΡΓΕΙΑ ΤΟΥΣ ΕΙΝΑΙ ΜΗΔΕΝ, ΜΠΟΡΕΙΣ ΝΑ ΕΛΕΓΧΕΙΣ ΑΜΕΣΑ ΤΙΣ ΠΡΑΞΕΙΣ ΤΟΥΣ

`bb({mouth:"smile", eyes:"normal"});`

n: ΔΙΑΛΕΞΕ ΤΗΝ ΤΕΛΙΚΗ ΚΙΝΗΣΗ ΣΟΥ

`bb({mouth:"small_lock", eyes:"fear"});`

n: *ΤΕΛΕΙΩΣΕ ΤΟΥΣ*

[{ΜΑΧΗ: Τιμώρησε το αγχωτικό σου τηλέφωνο!}](#act1i_phone) `Game.OVERRIDE_CHOICE_LINE=true`

[{ΦΥΓΗ: Μαζέψου σαν μπάλα και κλάψε!}](#act1i_cry) `Game.OVERRIDE_CHOICE_LINE=true`

# act1i_phone

`bb({mouth:"normal", eyes:"narrow"})`

b: Το τηλέφωνό σου σου έδινε κρίση πανικού!

`bb({eyes:"anger"})`

b: Ο Zuckerberg και η παρέα του κάνουν hijack την ψυχική σου υγεία για λεφτά venture capital!

```
bb({body:"fear", eyes:"fear"});
hong({body:"3_defeated2"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Τιμώρησε το τηλέφωνό σου! Κατάστρεψέ το! Σκότωσέ το!

```
Game.OVERRIDE_TEXT_SPEED = 2.5;
bb({body:"flail"});
hong({body:"3_defeated3"});
_.act1_ending = "fight";
```

b: ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚΟΤΩΣΕ ΤΟ ΣΚ--

(#act1j)

# act1i_cry

`bb({eyes:"fear", mouth:"normal"})`

b: Ολόκληρος ο κόσμος είναι γεμάτος κίνδυνο!

```
bb({body:"fear"});
hong({body:"3_defeated2"});
Game.OVERRIDE_TEXT_SPEED = 1.5;
```

b: Κάνε σαν το αρμαντίγιο! Μαζέψου σαν μπάλα για αυτοάμυνα!

```
Game.OVERRIDE_TEXT_SPEED = 2.5;
bb({body:"flail"});
hong({body:"3_defeated3"});
_.act1_ending = "flight";
```

b: ΜΑΖΕΨΟΥ ΚΑΙ ΚΛΑΨΕ ΜΑΖΕΨΟΥ ΚΑΙ ΚΛΑΨΕ ΜΑΖΕΨΟΥ ΚΑΙ ΚΛΑΨΕ ΜΑΖΕΨΟΥ ΚΑΙ ΚΛΑΨΕ ΜΑΖΕΨΟΥ ΚΑΙ ΚΛΑ-- 

(#act1j)

# act1j

`SceneSetup.act1_outro()`
