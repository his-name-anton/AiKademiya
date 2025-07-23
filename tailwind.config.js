module.exports = {
    darkMode: 'class',
    content: [
        './templates/**/*.html',
        './frontend/**/*.{vue,js}',
        // './aikademiya/**/*.py',
        // './assets/**/*.css',
        // './static/**/*.css',

        './node_modules/flowbite/**/*.js'
    ],
    plugins: [
        require('flowbite/plugin')
    ],
};
