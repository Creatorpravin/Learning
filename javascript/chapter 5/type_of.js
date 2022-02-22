typeof 10;//number
typeof 10n;//bigint
10n === BigInt(10);//true
10n == 10;//true
200n/20n;//10n
200n/20;//uncaught typeerror connont mic bigint and other type
-100n;//100n
+100n;//uncaught typeerror