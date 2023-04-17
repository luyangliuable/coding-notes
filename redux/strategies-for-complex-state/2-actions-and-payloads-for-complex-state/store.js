import allRecipesData from './data.js';

const initialState = {
    allRecipes: [],
    favoriteRecipes: [],
    searchTerm: ''
};

// Dispatched when the user types in the search input.
// Sends the search term to the store.
const setSearchTerm = (term) => {
    return {
        type: 'searchTerm/setSearchTerm',
        payload: term
    };
};

// Dispatched when the user presses the clear search button.
const clearSearchTerm = () => {
    return {
        type: 'searchTerm/clearSearchTerm'
    };
};

// Dispatched when the user first opens the application.
// Sends the allRecipesData array to the store.
const loadData = (type, payload) => {
    return {type: 'allRecipes/loadData', payload: allRecipesData};
};

// Dispatched when the user clicks on the heart icon of
// a recipe in the "All Recipes" section.
// Sends the recipe object to the store.
const addRecipe = (recipe) => {
    return {type: 'favoriteRecipes/addRecipe', payload: recipe};
};

// Dispatched when the user clicks on the broken heart
// icon of a recipe in the "Favorite Recipes" section.
// Sends the recipe object to the store.
const removeRecipe = (recipe) => {
    return {type: 'favoriteRecipes/removeRecipe', payload: recipe};
};


