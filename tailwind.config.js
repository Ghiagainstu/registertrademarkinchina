/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./dist/**/*.html', './dist/**/*.js'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#0FF0B3',
          50: '#E6FFF7',
          100: '#B3FFE8',
          200: '#80FFD9',
          300: '#4DFFCA',
          400: '#1AFFBB',
          500: '#0FF0B3',
          600: '#0CC08F',
          700: '#09906B',
          800: '#066048',
          900: '#033024',
        },
        surface: {
          DEFAULT: '#0B0F1A',
          50: '#1A1F2E',
          100: '#141925',
          200: '#0F1320',
          300: '#0B0F1A',
          400: '#070A14',
          500: '#04060D',
        },
        accent: {
          DEFAULT: '#00D4FF',
          dim: '#00D4FF33',
        },
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        body: ['"Inter"', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'grid-pattern': 'linear-gradient(rgba(15,240,179,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(15,240,179,0.03) 1px, transparent 1px)',
      },
      backgroundSize: {
        'grid': '40px 40px',
      },
      animation: {
        'glow': 'glow 3s ease-in-out infinite alternate',
        'float': 'float 6s ease-in-out infinite',
        'slide-up': 'slideUp 0.6s ease-out',
        'fade-in': 'fadeIn 0.8s ease-out',
      },
      keyframes: {
        glow: {
          '0%': { boxShadow: '0 0 20px rgba(15,240,179,0.3)' },
          '100%': { boxShadow: '0 0 40px rgba(15,240,179,0.6), 0 0 80px rgba(0,212,255,0.2)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        slideUp: {
          '0%': { transform: 'translateY(30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};
