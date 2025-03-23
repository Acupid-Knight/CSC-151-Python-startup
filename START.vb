START
    DEFINE constant WIDGET_PRICE as 4.79
    DEFINE constant BASE_SALARY as 2000

    INPUT salesperson's Antonio
    INPUT widgets sold
    INPUT widgets returned

    CALCULATE net widgets sold = widgets sold - widgets returned
    CALCULATE widget sales amount = net widgets sold * WIDGET_PRICE

    IF net widgets sold <= 100
        SET commission rate to 0.10 (10%)
    ELSE IF net widgets sold <= 199
        SET commission rate to 0.15 (15%)
    ELSE IF net widgets sold <= 299
        SET commission rate to 0.20 (20%)
    ELSE
        SET commission rate to 0.25 (25%)

    CALCULATE commission amount = commission rate * widget sales amount
    CALCULATE monthly salary = commission amount + BASE_SALARY

    OUTPUT salesperson's Antonio
    OUTPUT net widgets sold
    OUTPUT widget sales amount
    OUTPUT commission amount
    OUTPUT monthly salary
END

