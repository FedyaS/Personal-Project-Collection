Benford's Law is something that was mentioned in an AP Statistics textbook and I became very interested. The law basically states that the distribuition of the leading digits of datasets which span over multiple magnitudes and are naturally occuring will often be inversly distributed rather than uniformly. This makes sense because wherever you have exponential growth, it will take the greatest amount to grow from the 100s to 200s (200%) and less to grow from 200s to 300s (150%) and so on. Surprisingly, Benford's Law has a ton of applications and a lot of datasets match the distribution. The Wiki page is very interesting: https://en.wikipedia.org/wiki/Benford%27s_law.

I was curious to verify this law on my own so I took the list of the 314 top US Cities by population https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population and wrote a small python script to analyze the leading digits. The trend definitely exists as the 1s occur way more often than any other digit:

![image](https://user-images.githubusercontent.com/61990860/115141817-303b6400-9ff3-11eb-8a97-4e912e012be5.png)

However, I think this dataset is a bit biased since Wikipedia cut off their list by only including cities with a population of 100,000 or more (adding a lot of 1s).

The script is convenient because any dataset can be pasted into the .txt (with each point on a seperate line) and analyzed.
