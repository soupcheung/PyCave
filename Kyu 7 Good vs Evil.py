def goodVsEvil(good, evil):
    goods = [int(i) for i in good.split(' ')]
    evils = [int(i) for i in evil.split(' ')]
    goods[0] = goods[0] * 1
    goods[1] = goods[1] * 2
    goods[2] = goods[2] * 3
    goods[3] = goods[3] * 3
    goods[4] = goods[4] * 4
    goods[5] = goods[5] * 10

    evils[0] = evils[0] * 1
    evils[1] = evils[1] * 2
    evils[2] = evils[2] * 2
    evils[3] = evils[3] * 2
    evils[4] = evils[4] * 3
    evils[5] = evils[5] * 5
    evils[6] = evils[6] * 10

    if sum(goods) < sum(evils):
    	return ('Battle Result: Evil eradicates all trace of Good')
    elif sum(goods) > sum(evils):
    	return ('Battle Result: Good triumphs over Evil')
    elif sum(goods) == sum(evils):
    	return ('Battle Result: Should be a tie')

print (goodVsEvil('9 2 0 1 0 0', '2 9 3 8 5 10 10'))