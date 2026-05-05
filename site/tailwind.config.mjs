/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,ts,tsx,js,jsx,md}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // warm paper palette (light)
        paper: {
          50: '#fbf6ec',
          100: '#f7efdf',
          200: '#ede4d0',
          300: '#e0d5bc',
          400: '#c9bb9c',
        },
        ink: {
          50: '#f5f3ee',
          100: '#e9e6df',
          200: '#cfcbc1',
          300: '#a39e92',
          400: '#6b6759',
          500: '#4a473d',
          600: '#33312a',
          700: '#23211c',
          800: '#181712',
          900: '#0f0e0a',
        },
        // dark theme background — matches the screenshot
        nightbg: {
          DEFAULT: '#0f1217',
          soft: '#161a21',
        },
        // accent: muted cobalt that reads on both warm paper and dark navy
        accent: {
          DEFAULT: '#3057c4',
          dark: '#6b8cf0',
        },
        chip: {
          light: '#ece2cf',
          'light-hover': '#e1d3b6',
          dark: '#222732',
          'dark-hover': '#2c3240',
        },
      },
      fontFamily: {
        sans: [
          '"IBM Plex Sans"',
          'ui-sans-serif',
          'system-ui',
          '-apple-system',
          'Segoe UI',
          'Helvetica',
          'sans-serif',
        ],
        display: [
          '"Fraunces Variable"',
          'ui-serif',
          'Iowan Old Style',
          'Charter',
          'Georgia',
          'serif',
        ],
        serif: [
          '"Fraunces Variable"',
          'ui-serif',
          'Iowan Old Style',
          'Charter',
          'Georgia',
          'serif',
        ],
        mono: [
          '"IBM Plex Mono"',
          'ui-monospace',
          'SFMono-Regular',
          'Menlo',
          'Monaco',
          'monospace',
        ],
      },
      fontFeatureSettings: {
        'tabular-nums': '"tnum"',
      },
      maxWidth: {
        'reading': '72ch',
      },
      typography: ({ theme }) => ({
        DEFAULT: {
          css: {
            color: theme('colors.ink.700'),
            a: { color: theme('colors.accent.DEFAULT') },
          },
        },
      }),
    },
  },
  plugins: [],
};
