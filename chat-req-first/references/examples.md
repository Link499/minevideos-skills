# Chat-Req-First Examples

## Example 1: Mobile Layout Design

**User says:** "手机端不要左右分栏"

**Good confirmation:**
> **Layout Confirmation**
> 1. 直板手机：改为底部弹出面板，不左右分栏
> 2. 折叠屏：保持分栏，可切换手机模式
> 3. 操作台弹出方式：从底部滑入
>
> **To confirm:**
> 1. 操作台弹出后占屏幕多高？
> 2. 聊天框和操作台的位置关系？

**Bad response (no confirmation):**
> 好的，我已经把手机端改成了底部弹出面板。

## Example 2: Animation Effect

**User says:** "操作台从右下角弹出，像水波一样扩展开"

**Good confirmation:**
> **Animation Confirmation**
> - 起始点：右下角的发送按钮位置
> - 扩散方式：clip-path circle 从小到大
> - 最终大小：占屏幕 2/3 高度
>
> **To confirm:**
> 1. 扩散速度大约多快？0.3s? 0.5s?
> 2. 扩散完成后聊天框是否随后滑入？

**Bad response (assume and build):**
> 已实现水波扩散效果。

## Example 3: Style Reference

**User says:** "参考 iOS 26 的子页面弹出效果"

**Good confirmation:**
> **Style Reference Confirmation**
> 理解为 iOS 26 的 sheet 效果：
> - 顶部圆弧，可下拉隐藏
> - 半透明背景 + 模糊
> - 非全屏，露出底部内容
>
> **To confirm:**
> 1. 面板高度是固定还是可拖拽调整？
> 2. 下拉隐藏后是收起还是最小化？

**Bad response (guess the details):**
> 已实现 iOS 26 风格弹出。
