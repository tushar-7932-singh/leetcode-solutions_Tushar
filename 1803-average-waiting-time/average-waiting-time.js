/**
 * @param {number[][]} customers
 * @return {number}
 */
var averageWaitingTime = function(customers) {
    let currentTime = 0;
    let totalWaitingTime = 0;

    for (let i = 0; i < customers.length; i++) {
        let arrival = customers[i][0];
        let preparation = customers[i][1];

        if (currentTime < arrival) {
            currentTime = arrival;
        }

        currentTime += preparation;

        totalWaitingTime += currentTime - arrival;
    }

    return totalWaitingTime / customers.length;
};