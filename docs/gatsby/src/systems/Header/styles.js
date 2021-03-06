import { rem } from "utils/css";

const minWidthCalc = (t, space) => `calc(100% - ${rem(t.space[space])})`;

export const wrapper = {
  zIndex: 99,
  display: "flex",
  alignItems: "center",
  position: "absolute",
  top: 0,
  right: 0,
  minWidth: t => [minWidthCalc(t, 2), minWidthCalc(t, 3), minWidthCalc(t, 4)],
  bg: "header.bg",
  px: 3,
  py: 3,
  my: [2, 3, 4],
  borderRadius: `999px 0 0 999px`,
  boxShadow: "0 2px 15px rgba(0,0,0,0.15)"
};

export const right = {
  display: "flex",
  alignItems: "center",
  flex: 1
};

const toggleVisiblity = showing => ({
  visibility: [showing ? "hidden" : "visible", "visible"],
  width: [showing ? 0 : "auto", "auto"],
  opacity: [showing ? 0 : 1, 1],
  transition: "all .3s"
});

export const menuBtn = showing => ({
  ...toggleVisiblity(showing),
  mr: showing ? 0 : 2,
  display: ["flex", "flex", "none"],
  alignItems: "center",
  outline: "none",
  appearance: "none",
  background: "none",
  border: "none",

  ":hover": {
    cursor: "pointer"
  },

  svg: {
    stroke: "gray.3"
  }
});

export const logo = showing => ({
  ...toggleVisiblity(showing),
  width: [showing ? 0 : 60, 60, 80],
  height: [60, 60, 80]
});

export const socialIcons = showing => ({
  mr: [2, 2, 4],
  visibility: [showing ? "hidden" : "visible", "visible"],

  "a > svg": {
    stroke: "blue.3"
  },
  "a:hover > svg": {
    stroke: "blue.4"
  }
});
