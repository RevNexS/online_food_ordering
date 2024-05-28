document.querySelector('.scroll-button-left').addEventListener('click', () => {
    const categories = document.querySelector('.food-categories');
    categories.scrollBy({
        left: -200,
        behavior: 'smooth'
    });
});

document.querySelector('.scroll-button-right').addEventListener('click', () => {
    const categories = document.querySelector('.food-categories');
    categories.scrollBy({
        left: 200,
        behavior: 'smooth'
    });
});
