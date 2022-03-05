module.exports = {
  content: ["./website/campus_ambassador/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'open-sans': ["'Open Sans'", 'sans'],
        'montserrat': ["'Montserrat'", 'sans-serif'],
      },
      colors: {
        theme_clr: "var(--theme-color)",
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
};