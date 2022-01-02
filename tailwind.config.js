module.exports = {
  content: ["./website/campus_ambassador/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ["'Sarabun'",'sans-serif'],
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
};