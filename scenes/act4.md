# act4

```
SceneSetup.act4();
publish("SAVE_GAME", ["act4"]);
Game.FORCE_CANT_SKIP = true;
```

(...5001)

```
publish("set_how_many_prompts", [1]);
Game.FORCE_CANT_SKIP = false;
Game.CLICK_TO_ADVANCE = true;
```

n3: (αυτόματη αποθήκευση παιχνιδιού)

```
Game.clearText();
Game.FORCE_CANT_SKIP = true;
```

(...1001)

```
var hong_frame = _.INJURED ? 9 : 0;
publish("act4", ["hong_walks_in",hong_frame]);
sfx("grass_step1", {volume:0.1});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.2});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.25});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.3});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.35});
```

(...1667)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.35});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.35});
```

(...666)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step2", {volume:0.35});
```

(...1333)

```
publish("act4", ["hong_walks_in", "next"]);
sfx("grass_step1", {volume:0.20});
```

(...167)

```
publish("act4_hong_sits");
```

(...66)

```
publish("act4", ["hong_transition", "next"]);
sfx("squeak");
```

(...133)

`publish("act4", ["hong_transition", "next"]);`

(...1333)

```
publish("act4", ["hong_transition", "next"]);
sfx("rustle");
```

(...333)

`publish("act4", ["hong_transition", "next"]);`

(...1001)

```
publish("act4", ["hong_transition", "next"]);
```

(...333)

```
publish("act4", ["hong_transition", 9]);
sfx("sandwich");
```

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", 9]);`

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", 9]);`

(...333)

`publish("act4", ["hong_transition", 10]);`

(...333)

`publish("act4", ["hong_transition", "next"]);`

(...1466)

`publish("act4-out-1");`

(...201)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

`publish("act4", ["hong_transition", "next"]);`

(...99)

```
publish("act4-show-chars");
Game.FORCE_CANT_SKIP = false;
```

(...901)

`hong({body:"sigh_1"})`

(...601)

```
hong({body:"sigh_2"});
bb({eyes:"look_down"});
```

h: *αναστεναγμός*

```
hong({body:"hold", eyes:"normal", mouth:"normal"});
bb({eyes:"normal"});
```

h: Και λοιπόν, ποιο ^διάολο^ ήταν το ηθικό δίδαγμα αυτής της ιστορίας;

`hong({body:"one_up", eyes:"annoyed"})`

h: Τι *μάθαμε* καλά κιολάς; *Ήμουν* βλάκας, οι «φίλοι» μου με *εκμεταλλεύονταν*, και σχεδόν γαμώ *πεθάναμε*.

`hong({body:"normal", eyes:"normal"})`

{{if _.INJURED}}
[Ναι, κι αυτό χωρίς τον λογαριασμό του νοσοκομείου.](#act4a_bill)
{{/if}}

{{if !_.INJURED}}
[Ναι, κι αυτό χωρίς τη ζημιά στο συκώτι.](#act4a_liver)
{{/if}}

[Ναι, αυτό *ήταν* το χειρότερο σενάριο.](#act4a_worst)

[Ναι, είχα δίκιο.](#act4a_right)

# act4a_bill

`hong({eyes:"annoyed_l", mouth:"narrow"});`

h: Σωστά. Δεν νομίζω ότι η ασφάλειά μου καλύπτει «να είσαι ^βλάκας^».

`hong({eyes:"annoyed", mouth:"normal"});`

b: Κι όμως... επιβιώσαμε!

`hong({eyes:"normal"});`

h: ?

(#act4b)

# act4a_liver

`bb({eyes:"normal_d"});`

b: Σίγουρα μειώσαμε την προσδόκια ζωής μας κατά μερικά χρόνια...

`bb({eyes:"surprise"});`

b: Αλλά τουλάχιστον *έχουμε* ακόμα προσδόκια ζωής! Επιβιώσαμε!

```
hong({eyes:"surprise"});
bb({eyes:"normal"});
```

h: ?

(#act4b)

# act4a_worst

`bb({eyes:"normal_d"});`

b: Κι όμως...

h: Χμ;

`bb({eyes:"surprise"});`

b: Επιβιώσαμε!

(#act4b)

# act4a_right

`bb({eyes:"normal_d"});`

b: Αλλά... κι εσύ είχες δίκιο.

`hong({eyes:"surprise"});`

h: Χμ;

`bb({eyes:"normal"});`

b: Ήμουν ο λύκος που φώναζε «Λύκος!». Οπότε όταν ήρθε *πραγματικός* κίνδυνος, εσύ – δικαιολογημένα – δεν με *πίστεψες*.

`bb({eyes:"surprise_r"});`

b: Κι όμως, επιβιώσαμε!

(#act4b)

# act4b

```
bb({eyes:"normal", mouth:"normal"});
hong({eyes:"normal", mouth:"normal"});
```

b: Παρ' όλα αυτά, είμαστε ακόμα εδώ.

`hong({eyes:"suspect"});`

{{if _.INJURED}}
h: Φαίνεσαι αρκετά ήρεμος/η, σκέφτομαι ότι μόλις είχαμε μια εμπειρία κοντά στον θάνατο.
{{/if}}

{{if !_.INJURED}}
h: Φαίνεσαι αρκετά ήρεμος/η, σκέφτομαι ότι μόλις είχαμε μια εμπειρία *κοντά* στον κοντά-θάνατο.
{{/if}}

```
hong({eyes:"normal"});
bb({eyes:"annoyed_d", mouth:"narrow"});
```

b: Λοιπόν, κάνει όλα τα άλλα λιγότερο τρομακτικά σε σύγκριση. Με έβαλε κιόλας να σκέφτομαι.

`bb({eyes:"normal", mouth:"normal"});`

b: Αν το να σε πολεμώ είναι άχρηστο, γιατί δεν σε προστατεύει...

h: Αλλά το να σε πολεμώ *κιόλας* είναι άχρηστο, γιατί απλώς σε κάνει να φωνάζεις πιο δυνατά...

`bb({eyes:"normal_r"})`

b: Τότε ίσως...

`bb({eyes:"normal"})`

h: Ίσως δεν χρειάζεται να πολεμάμε.

```
Game.FORCE_CANT_SKIP = true;
Game.clearText();
```

(...301)

`publish("smash",[0]);`

(...2001)

```
publish("smash",[1]);
sfx("smash_glass");
```

(...2601)

```
publish("smash",[2]);
bb({eyes:"normal", mouth:"normal"});
hong({eyes:"normal", mouth:"normal"});
```

(...2001)

`Game.FORCE_CANT_SKIP = false;`

(#act4b_2)

# act4b_2

```
music('dontfight',{fade:5, volume:0.6});
bb({eyes:"annoyed_d"});
```

b: Δεν είμαι ο Μεγάλος Κακός Λύκος. Αλλά ούτε φρουρός-λύκος είμαι.

`bb({eyes:"sad_d"})`

b: Είμαι ένας κακοποιημένος σκύλος από καταφύγιο.

`bb({eyes:"sad"})`

b: Περάσαμε δύσκολα πράγματα. Ίσως τραύμα ή παραμέληση. Γι' αυτό μερικές φορές υπερβάλλω και πάω:

```
sfx("yaps", {volume:0.6});
bb({body:"yap_1"});
Game.FORCE_CANT_SKIP = true;
Game.WORDS_HEIGHT_BOTTOM = 215;
Game.FORCE_TEXT_DURATION = 90;
Game.FORCE_NO_VOICE = true;
```

b: ΓΑΥ ΓΑΥ ΓΑΥ ΓΑΥ ΓΑΥ

(...1884)

```
Game.WORDS_HEIGHT_BOTTOM = -1;
Game.FORCE_CANT_SKIP = false;
bb({body:"normal", mouth:"scream", eyes:"scream_sad"});
```

b: Αλλά δεν *θέλω* να είμαι δειλός σκύλος! Θέλω να σε προστατεύω! Θέλω να είμαι καλός σκύλος!

`bb({eyes:"sad", mouth:"normal"});`

b: Άνθρωπο... θα βοηθήσεις να εξημερώσουμε αυτόν τον λύκο;

`hong({eyes:"sad"})`

h: Ε... θα προσπαθήσω.

`hong({eyes:"normal_l", body:"chin", mouth:"narrow"})`

h: Εντάξει. Υγιής σχέση με τα συναισθήματα. Οι σχέσεις χρειάζονται επικοινωνία. Λοιπόν, ας επικοινωνήσουμε.

`hong({eyes:"normal", body:"hands_1", mouth:"normal"})`

h: Τα επόμενα πέντε λεπτά θα ακούγονται πολύ τυριά, αλλά ας το κάνουμε μέχρι να το πιστέψουμε.

```
hong({body:"hands_2", mouth:"normal"});
```

h: Αγαπητέ εσωτερικέ λύκε... πώς *νιώθεις*;

n2: ΣΥΝΟΛΟ ΦΟΒΩΝ ΠΟΥ ΧΡΗΣΙΜΟΠΟΙΗΘΗΚΑΝ:

n2: *ΒΛΑΒΗ* {{_.attack_harm_total}}, *ΜΗ ΑΓΑΠΗΜΕΝΟΥ* {{_.attack_alone_total}}, *ΚΑΚΟΣ* {{_.attack_bad_total}}

n2: ΓΙΑ ΠΟΙΟΝ ΦΟΒΟ ΘΕΛΕΙΣ ΝΑ ΜΙΛΗΣΟΥΜΕ ΠΡΩΤΑ; (ΤΟΥΣ ΑΛΛΟΥΣ ΜΠΟΡΕΙΣ ΜΕΤΑ)

```
_.a4_fears_discussed = 0;
_.num_thanks = 0;
hong({body:"normal"});
bb({eyes:"normal"});
```

[Φοβάμαι ότι θα βλαφτούμε.](#act4_harm)

[Φοβάμαι ότι θα μείνουμε μόνοι.](#act4_alone)

[Φοβάμαι ότι είμαστε κακοί άνθρωποι.](#act4_bad)

# act4_harm

```
_.a4_talked_about_harm = true;
_.a4_fears_discussed += 1;
```

`bb({eyes:"normal_d"})`

b: Θέλω να προστατεύσω την ανάγκη σου για σωματική ασφάλεια,

`bb({eyes:"sad_d"})`

b: Αλλά ο *ολόκληρος κόσμος* φαίνεται τόσο επικίνδυνος. Γεμάτος τραγωδία και κακία.

`bb({eyes:"sad"})`

{{if _.a4_fears_discussed==1}}
b: Δεν ξέρω, αρκετά με *εμένα* να διαλέγω τι θα πω μετά. Εσύ τι λες, *άνθρωπε*;
{{/if}}

{{if _.a4_fears_discussed==2}}
b: Πάλι, η σειρά σου, άνθρωπε. Τι πιστεύεις;
{{/if}}

{{if _.a4_fears_discussed==3}}
b: Άλλες σκέψεις, άνθρωπε;
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Έχεις δίκιο. Ας προστατευτούμε.](#act4_harm_skills)

[Ας εκθέσουμε τον εαυτό μας σε *περισσότερο* κίνδυνο.](#act4_harm_exposure)

[Ευχαριστώ.](#act4_thanks) `_.thanks_for = "physical safety";`

# act4_harm_skills

`bb({eyes:"look_down", body:"paw"})`

b: Αλλά... πώς; Έχω κυνόδοντες και νύχια, αλλά είμαι απλώς μεταφορά.

```
bb({ body:"normal", eyes:"normal" });
hong({ body:"one_up", eyes:"surprise" });
```

h: Μπορούμε να μάθουμε αυτοάμυνα; Να μπούμε σε κοινότητα που προστατεύει ο ένας τον άλλον; Να βελτιώσουμε την υγεία μας και τα προσωπικά μας όρια;

```
bb({ eyes:"annoyed_r" });
hong({ body:"normal", eyes:"normal" });
```

b: Ίσως, αλλά...

[Από πού ξεκινάμε καλά κιολάς;](#act4_harm_skills_start)

[Κι αν δεν δουλέψουν;](#act4_harm_skills_work)

[Κι αν το παρακάνουμε με την «ασφάλεια»;](#act4_harm_skills_overboard)

# act4_harm_skills_start

`bb({ eyes:"sad_d" })`

b: Υπάρχει τόσα πολλά να κάνουμε, τόσα που πρέπει να διορθώσουμε στον εαυτό μας. Με τι *αρχίζουμε* καλά κιολάς;

`hong({ body:"shrug", eyes:"surprise" })`

h: Αρχίζουμε τώρα.

`bb({ eyes:"normal", mouth:"narrow" })`

b: Ε;

```
bb({ body:"normal", mouth:"normal" });
hong({ body:"normal", mouth:"normal", eyes:"normal"});
```

h: Εξασκούμε καλή επικοινωνία αυτή τη στιγμή. Αυτό θα μας βοηθήσει να εντοπίζουμε καλύτερα τον κίνδυνο, με λιγότερα ψευδή θετικά,

`hong({ eyes:"surprise" });`

h: Και *αυτό* θα μας βοηθήσει να προστατευτούμε από βλάβη!

`hong({ eyes:"normal", mouth:"normal" });`

h: Άρα: αυτό *είναι* εκπαίδευση αυτοάμυνας.

`bb({ eyes:"normal_r" })`

b: Χμ. Περίμενα κάτι πιο τέτοιο:

```
Game.FORCE_CANT_SKIP = true;
Game.clearText();
hong({ eyes:"sad", mouth:"smile" });
bb({ body:"karate_1" });
sfx("hiya");
```

(...1001)

`Game.FORCE_CANT_SKIP = false;`

(#act4_something_else)

# act4_harm_skills_work

`bb({ eyes:"normal" });`

h: Σωστά, δεν υπάρχει τρόπος να προστατευτούμε 100%...

`hong({ body:"one_up" });`

h: Αλλά ακόμα κι ένα 1% βελτίωση αξίζει κάτι, έτσι δεν είναι;

```
bb({ eyes:"annoyed" });
hong({ normal:"one_up" });
```

b: Βλέπεις το ποτήρι όχι 99% άδειο, αλλά 1% γεμάτο;

`bb({ eyes:"normal" });`

h: Που ακόμα κι αυτό αξίζει κάτι αν έχεις αποκλειστεί στην έρημο.

`bb({ eyes:"closed" });`

b: Λοιπόν. Στην υγειά μας, τότε.

(#act4_something_else)

# act4_harm_skills_overboard

`bb({ body:"chest", eyes:"annoyed" })`

b: Εννοώ, ο λόγος που αγνόησες τις προειδοποιήσεις μου ήταν ότι *εγώ* το παρέκανε με την ασφάλεια! 

`bb({ body:"normal", eyes:"normal" })`

h: Όχι, έχεις δίκιο. Θα θέλαμε ασφάλεια με μέτρο. Όλα με μέτρο.

`bb({ eyes:"suspect" })`

b: Συγγνώμη, *ΟΛΑ* με μέτρο;

`hong({ eyes:"annoyed" })`

h: *Ένας μέτριος αριθμός πραγμάτων* με μέτρο.

```
bb({ eyes:"closed" });
hong({ eyes:"normal" });
```

b: Ευχαριστώ που έκανες τις δηλώσεις σου αναδρομικά αυτοσυνεπείς.

(#act4_something_else)


# act4_harm_exposure

`bb({ mouth:"scream_talk", eyes:"scream", MOUTH_LOCK:true });`

b: *ΤΙ*

```
bb({ mouth:"narrow", eyes:"suspect" });
hong({ body:"one_up" });
```

h: Εννοώ, ας πούμε ότι ένας σκύλος φοβάται την καταιγίδα.

`hong({ body:"hands_1" });`

h: Ένα κόλπο που χρησιμοποιούν οι εκπαιδευτές είναι να παίζουν ηχογράφηση βροντής σε χαμηλή ένταση, και μετά να δίνουν λιχουδιά στον σκύλο αν μείνει ήρεμος.

`hong({ body:"hands_2" });`

h: Σε μερικές μέρες, ο εκπαιδευτής ανεβάζει την ένταση λίγο-λίγο, μέχρι ο σκύλος να ξεπεράσει τον φόβο του για την καταιγίδα.

```
hong({ body:"normal", eyes:"surprise" });
bb({ mouth:"normal", eyes:"normal" });
```

h: Λέγεται θεραπεία έκθεσης!

`hong({ body:"point", eyes:"normal" });`

h: Εφόσον είσαι σκύλος, θα δούλευε κι εσένα, έτσι; Όλα τα θηλαστικά έχουν την ίδια αντίδραση πάλης-ή-φυγής.

`hong({ body:"normal" });`

[Κι αν αποευαισθητοποιηθούμε *πάρα* πολύ;](#act4_harm_exposure_overboard)

[Κι αν εκτεθούμε σε *πραγματικό* κίνδυνο;](#act4_harm_exposure_hurt)

[Είμαι λύκος, όχι σκύλος.](#act4_harm_exposure_dog) `bb({ eyes:"suspect" })`

# act4_harm_exposure_dog

h: Κι εγώ θα σου δείξω καλοσύνη και υπομονή μέχρι να εξημερωθείς σε χαριτωμένο μικρουδάκι.

`bb({ MOUTH_LOCK:true })`

b: ...

`bb({ eyes:"sad", mouth:"smile" })`

b: Ωχ.

(#act4_something_else)

# act4_harm_exposure_overboard

`bb({ eyes:"annoyed" })`

b: Μόλις *είδαμε* τι γίνεται αν κλείνεις τον φόβο σου – μπαίνεις σε *πραγματικά* επικίνδυνες καταστάσεις.

`bb({ eyes:"angry_r", body:"one_up" })`

b: Εξάλλου, δεν θα μας κάνει *υπερβολική* αποευαισθητοποίηση ψυχοπαθείς;

`bb({ mouth:"scream", eyes:"scream", body:"two_up" })`

b: Σύντομα θα μας δίνουμε λιχουδιές ενώ βλέπουμε snuff murder porn!

`hong({ eyes:"annoyed" })`

h: Ε... νομίζω υπάρχει μια γραμμή ανάμεσα σε αυτό και την καταιγίδα.

`bb({ body:"normal", mouth:"normal", eyes:"suspect" })`

b: Αλλά ακριβώς *πού*, άνθρωπε; *Πού;!*

`hong({ eyes:"surprise", body:"one_up" })`

h: Δεν ξέρω. Αλλά *εσύ* μπορείς να με βοηθήσεις!

`hong({ eyes:"normal", body:"normal" })`

h: Δουλεύοντας και διαπραγματευόμενοι μαζί σου, θα σχεδιάσουμε αυτή τη γραμμή.

`bb({ body:"paw", mouth:"narrow", eyes:"closed" })`

b: Εντάξει. Αλλά δεν έχω αντίθετους αντίχειρες, οπότε εσύ πρέπει να κάνεις το σχέδιο.

(#act4_something_else)

# act4_harm_exposure_hurt

`bb({ body:"two_up", eyes:"angry_r" })`

{{if _.INJURED}}
b: Για παράδειγμα: πηδήξαμε από μια γαμημένη *σκεπή!*
{{/if}}

{{if !_.INJURED}}
b: Για παράδειγμα: σχεδόν πηδήξαμε από μια γαμημένη *σκεπή!*
{{/if}}

```
hong({ eyes:"annoyed" });
bb({ body:"normal", eyes:"annoyed" });
```

h: Όχι, έχεις δίκιο. Μπορεί κανείς να το *παρακάνει*.

`hong({ eyes:"normal" });`

h: Αλλά γι' αυτό, αν κάνουμε θεραπεία έκθεσης, θα ξεκινήσουμε μικρά και θα ανεβαίνουμε σιγά-σιγά.

h: Λίγο πριν φτάσουμε σε *πραγματικό* κίνδυνο, σταματάμε.

`bb({ eyes:"annoyed_r", mouth:"narrow" });`

b: Ναι, εγώ βάζω τη γραμμή ανάμεσα στο να ακούς δυνατή βροντή και στο να στέκεις σε καταιγίδα με ψηλό μυτερό καπέλο.

(#act4_something_else)

# act4_thanks

`_.num_thanks += 1`

{{if _.num_thanks==1}}
(#act4_thanks_1)
{{/if}}

{{if _.num_thanks==2}}
(#act4_thanks_2)
{{/if}}

{{if _.num_thanks==3}}
(#act4_thanks_3)
{{/if}}

# act4_thanks_1

`bb({ MOUTH_LOCK:true })`

b: ...

`bb({ eyes:"annoyed" })`

b: Περίμενε, κανένα επιχείρημα υπέρ ή κατά αυτού που νιώθω; Απλώς... «ευχαριστώ»;

`hong({ eyes:"surprise", body:"shrug" })`

h: Ναι! Ευχαριστώ που έδειξες ότι σε νοιάζει η {{_.thanks_for}} μου.

```
bb({ eyes:"closed_annoyed", MOUTH_LOCK:true });
hong({ eyes:"normal", body:"normal" });
```

b: ...

h: Είσαι εντάξει;

`bb({ eyes:"super_sad", mouth:"narrow" });`

b: Δεν μου είχες πει ποτέ *ευχαριστώ* πριν.

`hong({ mouth:"smile" });`

h: Ω ρε μεγάλο μαλλιασμένο πανικολύκο.

(#act4_something_else)

# act4_thanks_2

h: Ακόμα κι αν υπερβάλλεις, εκτιμώ που φροντίζεις για την {{_.thanks_for}} μου.

`bb({ eyes:"annoyed" })`

b: Περίμενε... δεν επαναλαμβάνεις απλώς «ευχαριστώ» για να αποφύγεις να μιλήσουμε για αυτούς τους φόβους, έτσι;

```
bb({ eyes:"normal" });
hong({ eyes:"annoyed", body:"chin" });
```

h: Λοιπόν, τα πράγματα είναι περίπλοκα και δεν έχω πάντα έτοιμες απαντήσεις.

`hong({ eyes:"annoyed_l", body:"one_up" })`

h: Δεν είναι σαν η ζωή να σου δίνει λίστα με 3 έτοιμες απαντήσεις διαλόγου.

`hong({ eyes:"normal", mouth:"smile", body:"normal" })`

h: Αλλά προς το παρόν, μπορώ τουλάχιστον να πω ευχαριστώ.

b: Λοιπόν, κι εγώ ευχαριστώ που με άκουσες υπομονετικά.

`bb({ eyes:"closed" });`

b: Εσύ, μικρό γυμνό σαρκοθηλαστικό.

(#act4_something_else)

# act4_thanks_3

h: Ακόμα κι αν το γαύγισμά σου με τρομάζει, απλώς προσπαθείς να προστατεύσεις την {{_.thanks_for}} μου.

`bb({ eyes:"smile_r" });`

b: Εντάξει, αν συνεχίσεις να με κολακεύεις έτσι, το ίντερνετ θα βγάλει περίεργες ιδέες για μας.

```
bb({ eyes:"smile" });
hong({ eyes:"annoyed" });
```

h: Έλα, είμαι απλώς ένα ευάλωτο παιδί κολεγίου κι εσύ είσαι ένας μεγάλος, τρομακτικός λύκος. Τι χειρότερο μπορεί ν--

`hong({ eyes:"normal", body:"point" });`

h: Μάλλον, μην απαντήσεις.

(#act4_something_else)




# act4_alone

```
_.a4_talked_about_alone = true;
_.a4_fears_discussed += 1;
```

`bb({ eyes:"sad_d" });`

b: Θέλω να βεβαιωθώ ότι ικανοποιείς εκείνη τη βαθιά, ανθρώπινη ανάγκη να ανήκεις κάπου...

`bb({ eyes:"sad_u" });`

b: Αλλά φοβάμαι ότι αν κάποιος μάθαινε ποτέ τον *πραγματικό* μας εαυτό – θα μας τρόμαζαν όλοι.

`bb({ eyes:"sad" });`

{{if _.a4_fears_discussed==1}}
b: Δεν ξέρω, αρκετά με *εμένα* να διαλέγω τι θα πω μετά. Εσύ τι λες, *άνθρωπε*;
{{/if}}

{{if _.a4_fears_discussed==2}}
b: Πάλι, η σειρά σου, άνθρωπε. Τι πιστεύεις;
{{/if}}

{{if _.a4_fears_discussed==3}}
b: Άλλες σκέψεις, άνθρωπε;
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Συμφωνώ: ας δουλέψουμε την κοινωνική μας ζωή.](#act4_alone_skills)

[Νομίζω μας συμπαθούν. Ας το μάθουμε;](#act4_alone_experiment)

[Ευχαριστώ.](#act4_thanks) `_.thanks_for = "social belonging";`

# act4_alone_skills

```
bb({ eyes:"normal" });
hong({ body:"chin" });
```

h: Μπορούμε να εξασκηθούμε σε δεξιότητες όπως να κάνουμε ερωτήσεις, να ακούμε και να ενσυπαθούμε, να είμαστε ανοιχτοί και ευάλωτοι, κ.λπ.;

`hong({ eyes:"normal_l" });`

h: Ή να φτιάξουμε καλύτερες κοινωνικές συνήθειες, όπως να προγραμματίζουμε χρόνο με φίλους ή να πηγαίνουμε τακτικά σε meetups;

`hong({ body:"one_up" });`

h: Μπορούμε επίσης να μάθουμε να νιώθουμε πιο άνετα με την απόρριψη.

`hong({ eyes:"normal" });`

h: Ή να μάθουμε πότε οι άνθρωποι *δεν* μας απορρίπτουν, απλώς είναι κουρασμένοι ή έχουν Resting ^Bitch^ Face.

```
hong({ body:"normal" });
bb({ eyes:"annoyed_r" });
```

b: Αυτό είναι πολλές επιλογές. Αλλά, για το «μάθημα κοινωνικών δεξιοτήτων»...

[Δεν είναι αυτό *χειραγώγηση*;](#act4_alone_skills_manipulative)

[Δεν θα μας κάνει *πιο εύκολους στη χειραγώγηση*;](#act4_alone_skills_manipulated)

[Κι αν αποτύχουμε;](#act4_alone_skills_fail)

# act4_alone_skills_manipulative

`bb({ eyes:"suspect" });`

b: Δεν είναι οι σειριακοί δολοφόνοι που διαβάζουν τα συναισθήματα των θυμάτων τους τέλειοι στην «ενσυπάθεια»;

`bb({ eyes:"annoyed" });`

b: Δεν κέρδισε ο Charles Manson φίλους και επιρροή;

`hong({ eyes:"annoyed", body:"chin" });`

h: Όχι, έχεις δίκιο.

h: Οι «κοινωνικές δεξιότητες» δεν σημαίνουν τίποτα αν δεν νοιαζόμαστε *για* τους ανθρώπους.

`hong({ body:"normal" });`

h: Βασικά, απλώς μην είσαι ^μαλάκας^.

`bb({ eyes:"annoyed", mouth:"smile" });`

b: Αυτό είναι λεζάντα για αφίσα κινήτρου.

`hong({ body:"shrug", mouth:"narrow" });`

h: «Μην Είσαι ^Μαλάκας^™»

(#act4_something_else)

# act4_alone_skills_manipulated

`bb({ eyes:"angry" })`

b: Θα γίνουμε χαλάκι εισόδου που λέει Please and Thank You ενώ μας σκουπίζουν τα πόδια!

`bb({ mouth:"scream", eyes:"scream" })`

b: Θα φιλάμε τόσο πολύ κώλο που θα μοιάζουμε ότι φοράμε καφέ κραγιόν!

```
bb({ mouth:"normal", eyes:"normal" });
hong( body:"chin" });
```

h: Όχι, έχεις δίκιο. Οι «κοινωνικές δεξιότητες» δεν μπορούν να είναι μόνο για να ευχαριστείς τους άλλους, πρέπει να είναι και για να βάζεις *όρια.*

`hong( body:"one_up" });`

h: Δεν μπορούμε να καλέσουμε άλλους στο σπίτι μας, αν δεν έχουμε τοίχους να κρατήσουν το σπίτι μας.

```
hong( eyes:"angry", mouth:"narrow" });
bb( eyes:"annoyed", mouth:"smile" });
```

h: Επίσης... για εκείνη την εικόνα με το κραγιόν... *εεε??*

(#act4_something_else)

# act4_alone_skills_fail

`bb({ eyes:"annoyed" });`

h: Μπορεί να αποτύχουμε. Μάλιστα, *θα* αποτύχουμε.

```
bb({ eyes:"normal" });
hong({ eyes:"surprise", body:"shrug" });
```

h: Και αυτό είναι εντάξει! Η αποτυχία είναι πώς μαθαίνει κανείς οτιδήποτε νέο στην αρχή!

`hong({ body:"normal", eyes:"normal" });`

h: Λοιπόν ας αποτύχουμε μαζί και να προχωράμε, ε;

`bb({ eyes:"normal_r" });`

b: Εντάξει, νομίζω... χειρότερη περίπτωση, απλώς φεύγουμε πόλη και παίρνουμε νέα ταυτότητα.

`bb({ eyes:"normal" });`

h: Ναι, νομίζω αυτό κοστίζει μόνο δύο bitcoin αυτές τις μέρες.

(#act4_something_else)

# act4_alone_experiment

```
hong({ body:"one_up" });
bb({ eyes:"normal" });
```

h: Μπορούμε να δοκιμάσουμε μερικά πειράματα!

`hong({ body:"chin" });`

h: Μπορούμε να στείλουμε μήνυμα σε φίλο να βγούμε, να ξανασυνδεθούμε με παλιό φίλο, ή ακόμα κι απλώς να κουβεντιάσουμε με έναν barista.

`hong({ body:"normal" });`

h: Νομίζω μπορεί να ανακαλύψουμε ότι είμαστε πιο συμπαθητικοί απ' ό,τι υποψιαζόμαστε.

`bb({ eyes:"annoyed" });`

[Κι αν αυτά είναι μικρές, φτηνές «νίκες»;](#act4_alone_experiment_cheap)

[Κι αν είμαστε βάρος για τους άλλους;](#act4_alone_experiment_burden)

[Αλλά τα κουβένια δεν είναι ο *πραγματικός* μας εαυτός!](#act4_alone_experiment_real_us)

# act4_alone_experiment_real_us

`bb({ eyes:"sad" });`

b: Αν βάλουμε ρηχό χαμόγελο, δεν θα συνδεθούμε ποτέ πραγματικά με κανέναν,

`bb({ eyes:"super_sad" });`

b: *Αλλά* αν ανοίξουμε, οι άλλοι θα δουν όλα τα χαλασμένα εσωτερικά μας!

`hong({body:"chin", mouth:"narrow", MOUTH_LOCK:true})`

h: ...

```
hong({body:"normal", mouth:"normal"});
bb({eyes:"normal"});
```

h: Γύρνα.

b: Τι.

`hong({body:"hands_1"})`

h: Όταν οι σκύλοι θέλουν να δείξουν αγάπη και εμπιστοσύνη, κάνουν τον εαυτό τους ευάλωτο εκθέτοντας την κοιλιά τους.

`hong({body:"one_up"})`

h: Ίσως δεν είμαστε *ακόμα* αρκετά ασφαλείς για να είμαστε πολύ ευάλωτοι, αλλά με αρκετή εξάσκηση,

`hong({body:"normal", eyes:"surprise"})`

h: Μια μέρα μπορούμε να δείξουμε στους ανθρώπους τον πραγματικό μας εαυτό – όλο χαλασμένο, όλο ανθρώπινο.

```
hong({eyes:"normal"});
bb({ eyes:"super_sad", mouth:"smile", body:"chest" });
```

b: Θα γυρίσω αν μου δώσεις λιχουδιά.

`bb({ eyes:"normal", mouth:"normal" });`

h: Όχι.

(#act4_something_else)


# act4_alone_experiment_cheap

b: Το να πεις «γεια» στον barista δεν είναι ακριβώς χρυσό μετάλλιο στους Ολυμπιακούς Κοινωνικών Πεταλούδων.

```
hong({ body:"point", eyes:"surprise" });
bb({ eyes:"normal" });
```

h: Για *εμάς* είναι!

`hong({ body:"one_up", eyes:"annoyed" });`

h: Στην κοινωνική αρένα, δεν είμαστε καν featherweight, είμασαι σαν... quark-weight.

`hong({ body:"normal", eyes:"normal" });`

h: Αν πρέπει να ξεκινήσουμε με μικρές, φτηνές νίκες, έτσι να 'ναι. Πρέπει να ανέβεις το 1ο σκαλί πριν το 1000ο.

b: Ναι! Ίσως αφού πούμε «Γεια», να προχωρήσουμε στο...

`bb({ body:"two_up", mouth:"smile", eyes:"smile_u" });`

b: *«Τι κάνεις;»*

`hong({ body:"shrug", mouth:"smile", eyes:"surprise_l" });`

h: *«Όχι πολλά!»*

(#act4_something_else)

# act4_alone_experiment_burden

`bb({ eyes:"suspect_r" })`

b: Ίσως ο barista απλώς θέλει να φτιάξει τον καταραμένο καφέ του, όχι να είναι *πείραμα* για το αν οι κοινωνικές μας δεξιότητες αποτυγχάνουν.

`bb({ eyes:"annoyed" })`

h: Λοιπόν, αν τελικά *είμαστε* βάρος...

```
hong({ eyes:"surprise" });
bb({ eyes:"normal" });
```

h: Κι αυτό είναι καλό να το ξέρουμε!

`hong({ eyes:"normal" });`

h: Μπορούμε τότε να μάθουμε πώς να ρωτάμε προληπτικά τους ανθρώπους τι τους βολεύει, να γνωρίζουμε και να σεβόμαστε τα όρια των άλλων.

```
hong({ eyes:"annoyed_l", mouth:"narrow" });
bb({ eyes:"annoyed", mouth:"smile" });
```

h: Ξέρεις, όλα αυτά τα «διαπροσωπικά δεξιότητες» ^σκατά^ που βλέπουμε σε φυλλάδια συμβούλων.

(#act4_something_else)



# act4_bad

```
_.a4_talked_about_bad = true;
_.a4_fears_discussed += 1;
```

`bb({ eyes:"annoyed_r" })`

b: Θέλω να υπερασπιστώ τις ηθικές σου ανάγκες, αυτή την πίστη να γίνεσαι καλύτερος άνθρωπος,

`bb({ eyes:"sad_d" })`

b: Αλλά βαθιά μέσα μου νιώθω ότι είμαστε τόσο θεμελιωδώς... χαλασμένοι.

`bb({ body:"two_up", eyes:"angry" })`

{{if _.INJURED}}
b: Και μη μου πεις ότι *δεν* είμαστε χαλασμένοι. Πηδήξαμε από μια *σκεπή*.
{{/if}}

{{if !_.INJURED}}
b: Και μη μου πεις ότι *δεν* είμαστε χαλασμένοι. Σχεδόν πηδήξαμε από μια *σκεπή*.
{{/if}}

`bb({ body:"normal", eyes:"sad" })`

{{if _.a4_fears_discussed==1}}
b: Δεν ξέρω, αρκετά με *εμένα* να διαλέγω τι θα πω μετά. Εσύ τι λες, *άνθρωπε*;
{{/if}}

{{if _.a4_fears_discussed==2}}
b: Πάλι, η σειρά σου, άνθρωπε. Τι πιστεύεις;
{{/if}}

{{if _.a4_fears_discussed==3}}
b: Άλλες σκέψεις, άνθρωπε;
{{/if}}

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Άρα είμαστε χαλασμένοι. Ας μας φτιάξουμε.](#act4_bad_fix)

[Άρα είμαστε χαλασμένοι. Ας το αποδεχτούμε.](#act4_bad_accept)

[Ευχαριστώ.](#act4_thanks) `_.thanks_for = "moral well-being";`

# act4_bad_fix

```
bb({eyes:"normal"});
hong({body:"chin"});
```

h: Μπορούμε σιγά-σιγά να χτίσουμε καλύτερες συνήθειες, να ευθυγραμμίσουμε τη ζωή μας με αυτό που εκτιμούμε,

`hong({body:"one_up"});`

h: Κι αν χρειαστεί, μπορούμε να πάρουμε επαγγελματική βοήθεια – θεραπευτή ή σύμβουλο.

`hong({body:"normal"});`

h: Υπάρχουν τρόποι να μας φτιάξουμε.

[Κι αν δεν μπορούμε να τα φτιάξουμε όλα;](#act4_bad_fix_cant)

[Κι αν φτιάξουμε *πάρα* πολύ;](#act4_bad_fix_too_much)

[Δεν μας παίρνει η επαγγελματική βοήθεια.](#act4_bad_fix_afford)

# act4_bad_fix_cant

`hong({eyes:"annoyed"});`

h: Όχι, νομίζω έχεις δίκιο.

h: Δεν μπορούμε να τα φτιάξουμε όλα.

`bb({mouth:"scream", eyes:"scream_sad"});`

b: Ααα το ήξερα, θα είμαστε πάντα χαλασμένοι!

`hong({eyes:"surprise"});`

h: Αλλά μπορούμε τουλάχιστον να είμαστε *λιγότερο* χαλασμένοι.

```
bb({mouth:"normal", eyes:"annoyed"});
hong({eyes:"sad", mouth:"smile"});
```

h: Τα σημάδια επουλώνουν με τον καιρό, αλλά δεν εξαφανίζονται ποτέ. Και αυτό είναι εντάξει.

`bb({eyes:"annoyed_r"});`

b: Νομίζω. Εξάλλου,

```
Game.FORCE_TEXT_Y = 460;
Game.clearText();
publish("act4-sexy", [true]);
```

b: Τα σημάδια είναι *sexy.*

```
Game.FORCE_TEXT_Y = -1;
Game.clearText();
publish("act4-sexy", [false]);
bb({body:"chest", mouth:"smile_talk", MOUTH_LOCK:true, eyes:"sexy"}, 0);
hong({eyes:"normal", mouth:"normal"}, 0);
```

h: Μην το κάνεις αυτό.

(#act4_something_else)

# act4_bad_fix_too_much

`bb({ eyes:"angry_d" })`

b: Νιώθω άσχημα που το παραδέχομαι, αλλά... κάποιο μέρος μου *θέλει* να έχει αυτή τη διαταραχή.

`bb({ eyes:"angry" })`

b: Εννοώ, χωρίς αυτή, δεν θα είμαστε *βαρετοί*;

`bb({ eyes:"sad_r", body:"one_up" })`

b: Χωρίς τη διαταραχή, δεν θα σταματήσει η τέχνη μας να γίνεται ξινή και άχαμνη;

`bb({ eyes:"sad_u", body:"two_up" })`

b: Χωρίς τη διαταραχή, δεν θα μπορούμε να συνδεθούμε με τους φίλους μας που έχουν τη διαταραχή;

`bb({ eyes:"sad", body:"chest" })`

b: Αν είμαστε ποτέ ικανοποιημένοι με τη ζωή, δεν θα σταματήσουμε να ωθούμε τον εαυτό μας να κάνει σπουδαία πράγματα;

`hong({ MOUTH_LOCK:true })`

h: ...

h: Αν φοβόμαστε ακόμα κι... «να μας τελειώσουν οι φόβοι»...

h: Δεν νομίζω ότι θα μας τελειώσουν οι φόβοι.

`bb({ eyes:"smile_u", body:"normal", mouth:"smile" })`

b: Ω, ναι! Φιού! Τι ανακούφιση!

(#act4_something_else)

# act4_bad_fix_afford

`bb({ body:"one_up", eyes:"sexy", mouth:"normal" })`

b: «Γιατρέ, αγχώνομαι που πληρώνω 100$/ώρα απλώς για να μου ρωτάς *πώς σου κάνει αυτό;*»

`bb({ body:"paw", eyes:"closed", mouth:"narrow" })`

b: «Μμ-χμ. Και πώς σου κάνει αυτό;»

```
bb({ body:"normal", eyes:"normal", mouth:"normal" });
hong({ eyes:"sad" });
```

h: Όχι, αυτό είναι εντελώς λογικό άγχος.

`hong({ eyes:"annoyed", mouth:"sad" });`

h: Και πραγματικά γαμάει που η ψυχική υγεία δεν είναι προσιτή για πολλούς.

`hong({ eyes:"normal", mouth:"normal" });`

h: Παρ' όλα αυτά, υπάρχουν φτηνές ή δωρεάν επιλογές:

`hong({ body:"chin" })`

h: Ομάδες υποστήριξης, online θεραπεία, φοιτητικά/μη κερδοσκοπικά κέντρα υγείας...

`hong({ body:"hands_1" })`

h: Συνήθειες όπως διαλογισμός, καλός ύπνος, τακτική κουβέντα με φίλους, μάθηση νέων πραγμάτων...

`hong({ body:"hands_2" })`

h: Πήγαινε στη βιβλιοθήκη να δανειστείς βιβλία εργασίας για evidence-based ψυχοθεραπείες...

`hong({ body:"one_up" })`

h: Υπάρχει πλήρης λίστα πόρων στο τέλος αυτού του παιχνιδιού!

```
hong({ body:"normal" });
bb({ eyes:"annoyed", mouth:"narrow" });
```

b: Λοιπόν, *αυτός* ο τέταρτος τοίχος δεν κράτησε πολύ.

`hong({ body:"point" });`

h: Κάποια πράγματα είναι πιο σημαντικά από τις αφηγηματικές συμβάσεις. Όπως η ψυχική υγεία.

(#act4_something_else)


# act4_bad_accept

```
bb({ eyes:"normal" });
hong({ eyes:"normal_l", body:"one_up", mouth:"narrow" });
```

h: Εννοώ, αυτό λένε οι θεραπευτές, έτσι; Να αποδέχεσαι όλα τα συναισθήματά σου, ακόμα κι τα αρνητικά;

```
bb({ eyes:"annoyed" });
hong({ eyes:"normal", body:"normal", mouth:"normal" });
```

b: Περίμενε.

[«Αποδέχομαι» εννοώντας *παρατάω*;](#act4_bad_accept_give_up)

[«Αποδέχομαι» εννοώντας *εγκρίνω*;](#act4_bad_accept_approve)

[«Αποδέχομαι» εννοώντας *παίρνω κυριολεκτικά*;](#act4_bad_accept_literally)

# act4_bad_accept_give_up

`bb({ eyes:"angry", body:"one_up" });`

b: Νομίζεις ο Martin Luther King θα έλεγε, «Ωχ δεν μπορούμε να καθίσουμε μπροστά στο λεωφορείο, ας το *αποδεχτούμε*;»

`bb({ eyes:"angry_r", body:"two_up" });`

b: Γιατί ο Βιομηχανικός Συμπλέγματος Αυτοβοήθειας νομίζει ότι το να σηκώνεις λευκή σημαία είναι κάποια *βαθιά σοφία;*

`bb({ eyes:"annoyed", body:"normal" });`

h: Νομίζω οι θεραπευτές εννοούν «αποδέχομαι» τα κακά πράγματα ως: να αναγνωρίζεις ότι υπάρχουν και είναι δύσκολο να αλλάξουν,

h: Αλλά όχι απαραίτητα να παρατάς τη δέσμευση για αλλαγή.

`bb({ eyes:"suspect" });`

b: Τότε οι θεραπευτές θα έπρεπε να λένε *αναγνωρίζω*, όχι *αποδέχομαι*.

`hong({ body:"chin", eyes:"annoyed" });`

h: Ναι, τώρα που το σκέφτομαι, το «αποδέχομαι» είναι μπερδεμένο.

`bb({ eyes:"closed", mouth:"narrow" });`

b: Λοιπόν, το *αναγνωρίζω*.

(#act4_something_else)

# act4_bad_accept_approve

`bb({ eyes:"angry" });`

b: Σαν να είναι *καλό* που είμαστε χαλασμένοι ή κάτι; Όχι!

`bb({ eyes:"angry_r", body:"one_up" });`

b: Όλοι αυτοί οι καταραμένοι σεναριογράφοι του Χόλιγουντ που ρομαντικοποιούν την ψυχική αρρώστια είναι γεμάτοι σκατά!

`bb({ eyes:"angry", body:"two_up" });`

b: Το να έχεις ψυχική διαταραχή *γαμάει!* Κλέβει *ζωές* από ανθρώπους! Γιατί να το «αποδεχόμαστε»;

`bb({ body:"normal" });`

h: Νομίζω οι θεραπευτές εννοούν «αποδέχομαι» τα συναισθήματά μας ως: να είσαι υπομονετικός μαζί τους.

```
hong({ body:"one_up" });
bb({ eyes:"normal" });
```

h: Όπως όταν η πάλη στην αμμόλυση σε βυθίζει πιο γρήγορα, και η λύση είναι να ξαπλώσεις ήρεμα,

`hong({ eyes:"surprise" });`

{{if _.INJURED}}
h: Το να πολεμάω εσένα, τον φόβο μου, με έκανε να πηδήξω από μια σκεπή.
{{/if}}

{{if !_.INJURED}}
h: Το να πολεμάω εσένα, τον φόβο μου, σχεδόν με έκανε να πηδήξω από μια σκεπή.
{{/if}}

`hong({ body:"normal", eyes:"normal" });`

h: Αντίθετα, η λύση είναι να κάνουμε αυτό που κάνουμε τώρα – όχι να πολεμάμε, αλλά να είμαστε υπομονετικά μαζί.

`bb({ eyes:"annoyed" });`

b: Τότε θα έπρεπε να λένε *αυτό* αντί για κάποια προβληματική λέξη όπως «αποδέχομαι».

`hong({ body:"chin", eyes:"annoyed" });`

h: Ναι, τώρα που το σκέφτομαι, το «αποδέχομαι» γαμάει λίγο.

`bb({ eyes:"closed_annoyed", mouth:"narrow" });`

b: Δεν αποδέχομαι το «αποδέχομαι».

(#act4_something_else)

# act4_bad_accept_literally

`bb({ eyes:"sad", body:"one_up" });`

b: Αλλά *ξέρουμε* ήδη ότι δεν πρέπει να με παίρνεις κυριολεκτικά!

`bb({ eyes:"sad_u", body:"two_up" });`

b: Το *πρόβλημα* είναι ότι θέλω να σε βοηθήσω, αλλά αποτυγχάνω να το κάνω με λόγια!

`bb({ eyes:"sad", body:"normal" });`

h: Νομίζω οι θεραπευτές εννοούν «αποδέχομαι» τα συναισθήματά σου ως: «μην τα πολεμάς ή τα αγνοείς.»

`hong({ eyes:"surprise", body:"one_up" });`

h: Να σε ακούς, να δουλεύεις *μαζί* σου, αλλά να μην παίρνεις ό,τι λες ως 100% κυριολεκτική αλήθεια.

```
hong({ eyes:"normal", body:"normal" });
bb({ eyes:"annoyed", mouth:"normal" });`
```

b: Τότε οι θεραπευτές θα έπρεπε να λένε *αυτό* αντί για κάποια αόριστη μπερδεμένη λέξη όπως «αποδέχομαι».

`hong({ body:"chin", eyes:"annoyed" });`

h: Νομίζω κι εκείνοι αποτυγχάνουν με τα λόγια.

(#act4_something_else)




# act4_something_else

```
bb({ body:"normal", mouth:"normal", eyes:"normal" });
hong({ body:"normal", mouth:"normal", eyes:"normal" });
```

{{if _.a4_fears_discussed==1}}
h: Λοιπόν, κάτι άλλο θέλεις να πούμε;
{{/if}}

{{if _.a4_fears_discussed==2}}
h: Λοιπόν, κάτι άλλο στο βαρύ σου καρδιά;
{{/if}}

{{if _.a4_fears_discussed==3}}
(#act4_something_else_2)
{{/if}}

{{if _.a4_talked_about_harm!=true}}
[Φοβάμαι ότι θα βλαφτούμε.](#act4_harm)
{{/if}}

{{if _.a4_talked_about_alone!=true}}
[Φοβάμαι ότι θα μείνουμε μόνοι.](#act4_alone)
{{/if}}

{{if _.a4_talked_about_bad!=true}}
[Φοβάμαι ότι είμαστε κακοί άνθρωποι.](#act4_bad)
{{/if}}

[Όχι, είμαι εντάξει προς το παρόν.](#act4c_prelude)

# act4_something_else_2

h: Εντάξει, νομίζω μιλήσαμε για όλους τους φόβους μας τώρα.

b: Ναι, υπάρχουν μόνο τρεις φόβοι.

h: Ναι, ακριβώς τρεις.

b: Βολικό.

(#act4c)

# act4c_prelude

h: Καλή κουβέντα, ομάδα.

(#act4c)

# act4c

```
Game.clearText();
music(null,{fade:3});
bb({body:"normal", eyes:"normal", mouth:"normal", MOUTH_LOCK:true},0);
hong({body:"normal", eyes:"normal", mouth:"normal"},0);
```

b: ...

`hong({MOUTH_LOCK:true},0)`

h: ...

`bb({eyes:"annoyed_d"})`

b: Αυτό δεν είναι κάποιο *παιχνίδι*, ξέρεις.

`bb({eyes:"angry_d", body:"one_up"})`

b: Το να χτίσεις υγιή σχέση με τα συναισθήματά σου δεν είναι τόσο απλό όσο να πατάς κουμπιά σε μια οθόνη.

`bb({eyes:"sad", body:"normal"})`

b: *Μπορούμε* πραγματικά να τα βρούμε;

b: *Μπορούμε* να δουλέψουμε μαζί, σαν ομάδα;

`hong({eyes:"sad", body:"one_up"})`

h: Λοιπόν,

```
hong({eyes:"surprise_l"});
bb({eyes:"normal"});
```

a: Σ-συγγνώμη...

```
Game.clearText();
publish("act4-in-2");
music('campus', {volume:0.5, fade:1});
```

(...2101)

(#act4d)

# act4d

`Game.WORDS_HEIGHT_BOTTOM = 221;`

`publish("act4", ["alshire", 0]);`

a: Θ-θα σ' πείραζε αν κάθισα μαζί σου για μεσημεριανό;

`publish("act4", ["alshire", 1]);`

{{if _.TOP_FEAR=="harm"}}
s: *Αυτό* είναι το crush σου; Γιατί κάθονται μόνοι/η σαν ψυχοπαθής σειριακός δολοφόνος;
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: Να ρωτήσεις το crush σου αν μπορείς να καθίσεις μαζί τους; Ξέρεις πόσο *επιεικείς* ακούγόμαστε;
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: *Αυτό* είναι το crush σου; Διακόψαμε την ησυχία τους! Είμαστε τέτοιο βάρος!
{{/if}}

`publish("act4", ["alshire", 2]);`

a: Ε- εννοώ- εντάξει αν όχι, απλώς...

`publish("act4", ["alshire", 3]);`

`Game.OVERRIDE_CHOICE_SPEAKER = "h2"`

[Περίμενε, δεν σε είδα στο πάρτι;](#act4d_recognition) `publish("act4", ["hong_to_alshire",1])`

[Ναι, φυσικά! Έλα εδώ.](#act4d_yes) `publish("act4", ["hong_to_alshire",2])`

[Συγγνώμη, χρειάζομαι χρόνο μόνος/η τώρα.](#act4d_no) `publish("act4", ["hong_to_alshire",8])`

# act4d_recognition

`publish("act4", ["hong_to_alshire",2]);`

h2: Ναι, ήσουν στον καναπέ! Στο πρώτο πάρτι που πήγα...

`publish("act4", ["hong_to_alshire",10]);`

{{if _.a2_ending=="fight"}}
h2: Όπου είχα εκείνο το κρίση πανικού και χτύπησα τον οικοδεσπότη.
{{/if}}

{{if _.a2_ending=="flight"}}
h2: Όπου είχα εκείνο το κρίση πανικού και έφυγα κλαίγοντας.
{{/if}}

```
publish("act4", ["hong_to_alshire", 0]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: Περίμενε άνθρωπε, μπορεί να τους κάνουμε άβολα.

```
publish("act4", ["hong_to_alshire", 3]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: Α, δεν θέλω να σε βάλω σε δύσκολη θέση!

`publish("act4", ["hong_to_alshire",4]);`

h2: Απλώς θυμήθηκα ένα φιλικό πρόσωπο, τίποτα άλλο.

```
publish("act4", ["hong_to_alshire",5]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: ΑΑΑΑΑ ΤΟ ΞΕΡΩ! ΕΙΝΑΙ ΕΠΙΚΙΝΔΥΝΟΣ ΨΥΧΟΠΑΘΗΣ ΠΑΝΙΚΟΥ!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: ΑΑΑΧΗ Η ΠΡΩΤΗ ΕΝΤΥΠΩΣΗ ΠΟΥ ΚΑΝΑΜΕ ΗΤΑΝ «ΕΙΔΑΝ ΤΟ ΤΡΑΥΜΑ ΜΟΥ»! ΑΥΤΟ ΣΗΜΑΙΝΕΙ ΜΑΣ ΜΙΣΟΥΝ!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: ΑΑΑΧΗ ΚΑΝΑΜΕ ΚΑΠΟΙΟΝ ΝΑ ΘΥΜΗΘΕΙ ΤΡΑΥΜΑΤΙΚΟ ΓΕΓΟΝΟΣ. Η ΑΠΛΗ ΜΑΣ ΠΑΡΟΥΣΙΑ ΠΛΗΓΩΝΕΙ ΑΛΛΟΥΣ.
{{/if}}

(#act4e)

# act4d_yes

```
publish("act4", ["hong_to_alshire", 5]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: Περίμενε άνθρωπε, φαίνονται άβολα.

```
publish("act4", ["hong_to_alshire", 6]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: Α, καμία πίεση φυσικά!

`publish("act4", ["hong_to_alshire", 4]);`

h2: Απλώς λέω, μπορείς να καθίσεις εδώ αν θέλεις.

```
publish("act4", ["hong_to_alshire", 5]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: ΕΙΝΑΙ *ΠΟΛΥ* ΦΙΛΙΚΟΙ! ΣΑΝ ΤΟΝ TED BUNDY, ΤΟΝ ΣΕΙΡΙΑΚΟ ΔΟΛΟΦΟΝΟ!
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: ΑΠΛΩΣ ΠΡΟΣΠΟΙΟΥΝΤΑΙ ΕΥΓΕΝΙΚΟΙ! ΚΑΝΕΙΣ *ΠΡΑΓΜΑΤΙΚΑ* ΔΕΝ ΘΕΛΕΙ ΝΑ ΕΙΝΑΙ ΚΟΝΤΑ ΜΑΣ!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: ΑΑΑΧΗ ΠΑΝΤΑ ΚΑΝΟΥΜΕ ΤΟΥΣ ΑΛΛΟΥΣ ΝΑ ΝΙΩΘΟΥΝ ΑΝΕΝΤΟΜΟΙ! ΕΙΜΑΣΤΕ ΚΗΛΙΔΑ ΣΤΗ ΓΗ!
{{/if}}

(#act4e)

# act4d_no

```
publish("act4", ["hong_to_alshire", 9]);
publish("act4", ["bb_to_alshire", _.INJURED ? 3 : 1]);
```

b: Περίμενε άνθρωπε, μπορεί να τους κάνουμε άβολα.

```
publish("act4", ["hong_to_alshire", 3]);
publish("act4", ["bb_to_alshire", _.INJURED ? 2 : 0]);
```

h2: Α, δεν θέλω να είμαι αγενής!

`publish("act4", ["hong_to_alshire", 6]);`

h2: Απλώς χρειάζομαι λίγο χρόνο να επεξεργαστώ τα συναισθήματά μου. Μην το πάρεις προσωπικά.

```
publish("act4", ["hong_to_alshire", 7]);
publish("act4", ["alshire", 4]);
```

{{if _.TOP_FEAR=="harm"}}
s: ΤΙ ΑΡΡΩΣΤΕΣ, ΣΤΡΕΒΛΩΜΕΝΕΣ ΣΚΕΨΕΙΣ ΕΠΕΞΕΡΓΑΖΟΝΤΑΙ; ΤΙ ΣΚΟΤΕΙΝΕΣ ΕΠΙΘΥΜΙΕΣ ΓΕΜΙΖΟΥΝ ΤΗΝ ΚΑΡΔΙΑ ΑΥΤΟΥ ΤΟΥ ΨΥΧΟΠΑΘΗ;
{{/if}}

{{if _.TOP_FEAR=="alone"}}
s: ΜΑΣ ΑΠΟΡΡΙΨΑΝ ΠΡΟΣΩΠΙΚΑ! ΔΕΝ ΘΑ ΑΓΑΠΗΘΟΥΜΕ ΠΟΤΕ!
{{/if}}

{{if _.TOP_FEAR=="bad"}}
s: ΔΙΕΚΟΨΑΜΕ ΤΗΝ ΕΠΕΞΕΡΓΑΣΙΑ ΣΥΝΑΙΣΘΗΜΑΤΩΝ ΤΟΥΣ! ΤΩΡΑ ΘΑ ΤΡΑΥΜΑΤΙΣΤΟΥΝ ΓΙΑ ΠΑΝΤΑ ΚΑΙ ΕΙΝΑΙ ΟΛΑ ΔΙΚΗ ΜΑΣ ΕΥΘΥΝΗ!
{{/if}}

(#act4e)

# act4e

```
Game.WORDS_HEIGHT_BOTTOM = 195;
publish("act4", ["alshire", 6]);
```

s: ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ ΤΡΕΧΕ

```
Game.clearText();
publish("act4", ["hong_to_alshire", 0]);
publish("act4", ["alshire", 10]);
sfx("pop");
```

(...1001)

```
publish("act4", ["alshire", 11]);
sfx("alshire_run");
```

(...2601)

```
publish("act4-out-3");
Game.WORDS_HEIGHT_BOTTOM = -1; /* reset */
```

(...1201)

`publish("act4-jumpcut-hong");`

h: Χμ. Ήταν περίεργο. Αναρωτιέμαι τι περνούσε από το κεφάλι τους.

`publish("act4", ["hong_closer", 2]);`

h: Λοιπόν, έλεγες;

```
publish("act4", ["hong_closer", 1]);
publish("act4", ["bb_closer", 6]);
```

b: Ε, ξέχασα; Κάτι για ομάδες και δουλειά;

```
publish("act4", ["bb_closer", 0]);
publish("act4", ["hong_closer", 3]);
```

h: ¯\_(ツ)_/¯

```
publish("act4", ["hong_closer", 1]);
publish("act4", ["bb_closer", 4]);
```

b: Λένε ότι πρέπει να «κάνεις ειρήνη» με τα συναισθήματά σου, σαν να είναι *εγκληματίες πολέμου*.

`publish("act4", ["bb_closer", 7]);`

b: Αλλά θέλω να κάνουμε *περισσότερα* από απλή ειρήνη! Θέλω να είμαστε *σύμμαχοι!*

`publish("act4", ["bb_closer", 3]);`

b: Θέλω να είμαι καλός φρουρός-σκύλος. Όπως η πείνα και η δίψα είναι συναγερμοί για τις σωματικές σου ανάγκες,

`publish("act4", ["bb_closer", 8]);`

b: Θέλω να είμαι ο συναγερμός για τις *ψυχολογικές* σου ανάγκες – τις ανάγκες σου για ασφάλεια, ανήκειν, καλοσύνη.

`publish("act4", ["bb_closer", 1]);`

b: Αλλά... αποτυγχάνω στη δουλειά μου, οπότε χρειάζομαι εσένα να με εκπαιδεύσεις.

`publish("act4", ["bb_closer", 4]);`

b: Δεν είμαι «πάντα έγκυρος/η», ούτε «πάντα παράλογος/η». Απλώς... προσπαθώ όσο μπορώ. Λοιπόν, παρακαλώ,

`publish("act4", ["bb_closer", 30]);`

b: Βοήθησέ με να σε βοηθήσω!

`publish("act4", ["bb_closer", 6]);`

b: Όμως, το να μάθεις σε γέρο σκύλο νέα κόλπα *θα* πάρει καιρό. Ίσως *χρόνια.*

`publish("act4", ["bb_closer", 3]);`

b: Και μερικές φορές θα υποτροπιάσω, θα γλιστρήσω στις παλιές μου συνήθειες.

`publish("act4", ["bb_closer", 2]);`

b: Θα γαυγίζω σε σκιές. Θα σε τρομάζω με λόγια. Μπορεί ακόμα κι να σου δείξω ενοχλητικές εικόνες... πραγμάτων.

`publish("act4", ["bb_closer", 9]);`

b: Συγγνώμη! Είμαι κακοποιημένος σκύλος από καταφύγιο! Οι κακοποιημένοι σκύλοι κάνουν καμάκι στο κρεβάτι σου μερικές φορές!

`publish("act4", ["bb_closer", 4]);`

b: Αλλά αν είσαι υπομονετικός/ή μαζί μου... και απλώς μείνεις και κάτσεις μαζί μου...

`publish("act4", ["bb_closer", 8]);`

b: Ίσως μπορέσεις να εξημερώσεις αυτόν τον λύκο.

`publish("act4", ["bb_closer", 0]);`

`Game.clearText();`

(...1000)

`Game.OVERRIDE_CHOICE_SPEAKER = "h"`

[Καλός σκύλος.](#act4f-pat-bb) `Game.OVERRIDE_CHOICE_SPEAKER = "h"; publish("act4", ["hong_closer", 2]);`

`Game.OVERRIDE_CHOICE_SPEAKER = "b"`

[Καλός άνθρωπος.](#act4f-pat-hong) `Game.OVERRIDE_CHOICE_SPEAKER = "b"; publish("act4", ["bb_closer", 8]);`

# act4f-pat-hong

```
Game.clearText();
publish("hide_tabs");
Game.FORCE_CANT_SKIP = true;
music(null,{fade:0.5});
sfx("youbothwin");
```

```
publish("act4", ["hong_closer", 4]);
publish("act4", ["bb_closer", 13]);
```

(...501)

`publish("act4", ["bb_closer", 14]);`

(...501)

`publish("act4", ["bb_closer", 13]);`

(...501)

`publish("act4", ["bb_closer", 14]);`

(...501)

`publish("act4", ["bb_closer", 13]);`

(...501)

`publish("act4", ["bb_closer", 14]);`

(...6501)

`publish("act4", ["bb_closer", 15]);`

(...1001)

(#act4f)

# act4f-pat-bb

```
Game.clearText();
publish("hide_tabs");
Game.FORCE_CANT_SKIP = true;
music(null,{fade:0.5});
sfx("youbothwin");
```

```
publish("act4", ["hong_closer", 4]);
publish("act4", ["bb_closer", 10]);
```

(...501)

`publish("act4", ["bb_closer", 11]);`

(...501)

`publish("act4", ["bb_closer", 10]);`

(...501)

`publish("act4", ["bb_closer", 11]);`

(...501)

`publish("act4", ["bb_closer", 10]);`

(...501)

`publish("act4", ["bb_closer", 11]);`

(...6501)

`publish("act4", ["bb_closer", 12]);`

(...1001)

(#act4f)

# act4f

```
Game.FORCE_CANT_SKIP = false;
publish("act4", ["bb_closer", 16]);
publish("act4", ["hong_closer", 5]);
```

{{if _.fifteencigs}}
b: ΑΑΑΑΑ ΑΚΟΜΑ ΤΡΩΣ ΜΟΝΟΣ/Η ΠΕΝΤΕΝΗΜΕΡΙΑ ΤΣΙΓΑΡΑ ΑΑΑΑΑ
{{/if}}

{{if _.parasite}}
b: ΑΑΑΑΑ ΑΚΟΜΑ ΔΕΝ ΕΙΣΑΙ ΠΑΡΑΓΩΓΙΚΟΣ/Η ΕΝΩ ΤΡΩΣ ΕΙΜΑΣΤΕ ΠΑΡΑΣΙΤΑ-ΚΟΙΝΩΝΙΑΣ ΑΑΑΑΑ
{{/if}}

{{if _.whitebread}}
b: ΑΑΑΑΑ ΤΡΩΣ ΑΚΟΜΑ ΛΕΥΚΟ ΨΩΜΙ ΑΑΑΑΑ
{{/if}}

```
publish("act4", ["bb_closer", 18]);
publish("act4", ["hong_closer", 6]);
sfx("yaps", {volume:0.6});
Game.FORCE_CANT_SKIP = true;
Game.WORDS_HEIGHT_BOTTOM = 205;
Game.FORCE_TEXT_DURATION = 90;
Game.FORCE_NO_VOICE = true;
```

b: ΓΑΥ ΓΑΥ ΓΑΥ ΓΑΥ ΓΑΥ

(#credits)
