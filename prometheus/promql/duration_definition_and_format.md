# Duration definition and format
In promQL, some function take some duration specifiers (such as `xxx_over_time` functions).
Such durations are expressed as shown below:

```
[range:resolution] offset <duration> @<Unix_timestamp>
```

- `range`: continuous interval of scrapes used as entry set for a function.
    range is defined using a duration (now - range value). 
    This parameter is `mandatory`.
- `resolution`: offset between each scrape to be selected in range.
    This parameter discretizes the interval into a discrete set of scrapes.
    By default, prometheus scraping interval is used (30 seconds).
    Example:
        ```
        sum_over_time(my_metric[24h:1h])
        ```
        Sums all scrapes from now to now-24h.
        Thanks to the resolution, only 24 scrapes will be selected.
        That is, one per hour.
- `offset`: offset from the time origin (`0s` by default). It is a `duration`.
- `@`: define the time origin (default is `now`). This value is an `unix timestamp`.

