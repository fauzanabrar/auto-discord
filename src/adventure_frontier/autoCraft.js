// This script automates the clicking of the "Craft again" button in a web application.

function clickCraftAgainButton(times = 10) {
    let count = 0;

    const interval = setInterval(() => {
        const button = [...document.querySelectorAll('button')].find(btn =>
            btn.textContent.trim() === 'Craft again'
        );

        if (button) {
            button.click();
            count++;
            console.log(`Clicked ${count} time(s)`);
        } else {
            console.warn('Craft again button not found');
            clearInterval(interval);
        }

        if (count >= times) {
            clearInterval(interval);
            console.log('Done clicking');
        }
    }, 1500); // adjust delay as needed to avoid over-clicking too fast
}

clickCraftAgainButton(10); // Call the function with the desired number of clicks