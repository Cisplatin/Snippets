print (1..20).map{|n| (2..n).select{|i| n % i == 0}}
