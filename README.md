# blogger访问量数据抓取
blogger第一代经典模板不能像第二代布局模板通过添加统计信息的小工具显示博客的访问量，而我又不太喜欢第二代模板，第二代预设的样式无法去除，即使你把模板html全部删了，也会给你添加一些东西，非常影响模板样式的自定义。本代码通过blogger api获取博客访问量数据，保存为json格式，方便在模板中通过Javascript读取并呈现在页面中。
使用github action每隔一段时间执行一次，也就是说最终博客呈现的访问量统计数据并不是实时更新的，这个更新的频率取决于设置的间隔时间。我觉得半小时就差不多了，甚至一小时或者一天都可以，访客其实对这数据不太在意，自己如果想看实时的可以登录blogger后台。
