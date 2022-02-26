module.exports = {
  content: ["./website/campus_ambassador/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'open-sans': ["'Open Sans'", 'sans'],
        'montserrat': ["'Montserrat'", 'sans-serif'],
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
};