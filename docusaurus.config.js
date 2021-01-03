module.exports = {
  title: "Computerization Sponsorship",
  tagline: "Website for Computerization Sponsorship agreement docs",
  url: "https://computerization-sponsorship.developersam.com",
  baseUrl: "/",
  favicon: "https://developersam.com/favicon.ico",
  themeConfig: require("./theme-config.json"),
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.json"),
          routeBasePath: "/",
          editUrl: "https://github.com/sam-foundation/computerization-sponsorship/edit/master/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
};
