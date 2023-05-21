
  module.exports = async () => {
    return {
      verbose: true,
      transformIgnorePatterns: [
        "/node_modules/",
      ],
      moduleNameMapper: {
        ".+\\.(css|scss|png|jpg|svg)$": "jest-transform-stub"
      }
    };
  };