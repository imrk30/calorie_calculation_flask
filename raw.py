carbs = float(input('Enter carbohydrates (in grams) :'))
proteins = float(input('Enter proteins (in grams) :'))
fats = float(input('Enter fats (in grams) :'))

cc = carbs * 4
cp = proteins * 4
cf = fats * 9
ct = cc+cp+cf

print('Calories in carbohydrates '+str(cc)+' kcal'+
    '\nCalories in proteins '+str(cp)+' kcal'+
    '\nCalories in fats '+str(cf)+' kcal'+
    '\nTotal Calories is '+str(ct)+' kcal')