"""Build the static Arabic service site into dist/ with no runtime dependencies."""
from __future__ import annotations

import html
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
SITE = os.getenv("SITE_URL", "https://abu-mohamed-plumbing.vercel.app").rstrip("/")
NAME = "أبو محمد سباك وكهربائي"
PHONE = "0576879421"
E164 = "+966576879421"
WA = "https://wa.me/966576879421"
GOOGLE_SITE_VERIFICATION = "KroRbLNToQQ_EEKCW_vcDeheVi0wmUlSOi8uiAHqGAU"
BASE_AREA = "حي المصيف، الرياض"
CITY = "الرياض"
SERVICE_MODE = "ننتقل إلى مواقع العملاء داخل الرياض لتنفيذ الخدمة. مقر إدارة النشاط لا يستقبل العملاء."
LAST_UPDATED = "2026-10-12"

SERVICES = [
    dict(slug="leak-repair", category="plumbing", icon="drop", title="كشف وإصلاح تسربات المياه", short="تتبّع مصدر التهريب ومعالجة المواسير والوصلات والمحابس وفق حالة الموقع.",
         intro="بقعة رطوبة على الجدار، ارتفاع غير معتاد في استهلاك المياه، أو تنقيط مستمر أسفل المغسلة؛ كلها إشارات تستحق فحصًا مبكرًا. نقدم خدمة فحص وإصلاح تسربات المياه في الرياض بدءًا من تحديد المكان المحتمل للتسرب، ثم اختيار طريقة الإصلاح المناسبة للأنبوب أو الوصلة أو المحبس المتأثر.",
         detail="قد يظهر التسرب حول الخلاطات والسيفونات والسخانات، وقد يكون داخل تمديدات الحمام أو المطبخ. يبدأ التعامل مع الحالة بفهم وقت ظهور المياه ومكانها، وفحص الأجزاء الظاهرة والتوصيلات القريبة قبل تقرير ما إذا كانت المشكلة تحتاج استبدال قطعة، إعادة إحكام وصلة، أو معالجة جزء من التمديد. تختلف طريقة الفحص وحدود العمل بحسب إمكانية الوصول وطبيعة العطل، ولذلك لا نعِد بكشف كل حالة من دون فتح أو بتحديد التكلفة قبل المعاينة.",
         includes=["فحص الوصلات والمحابس والخلاطات الظاهرة", "معالجة تهريب الأنابيب بحسب موضع العطل", "استبدال القطع التالفة عند الحاجة بعد توضيحها", "مراجعة موضع الإصلاح وتشغيل المياه"],
         cases=["رطوبة حول المغسلة أو المرحاض", "تنقيط متكرر من السخان أو الخلاط", "تسرب ظاهر في تمديدات المطبخ أو الحمام"]),
    dict(slug="drain-unclogging", category="plumbing", icon="pipe", title="تسليك المجاري والبالوعات", short="معالجة بطء التصريف وانسداد الأحواض والبالوعات وخطوط الصرف المنزلية.",
         intro="عندما يتأخر نزول الماء من الحوض أو تظهر رائحة غير مألوفة من البالوعة، قد يكون السبب تراكمًا في السيفون أو انسدادًا أعمق في خط الصرف. تقدم خدمة تسليك المجاري والبالوعات بالرياض فحصًا لمكان الانسداد ثم معالجة تتناسب مع نوع الأنبوب وموضع المشكلة.",
         detail="نبدأ بمراجعة نقاط الصرف الأقرب إلى المشكلة: حوض المطبخ، مغسلة الحمام، أرضية الدش، أو بالوعة الأرضية. يساعد تمييز الانسداد الموضعي من تعطل أكثر من مصرف على اختيار طريقة التعامل المناسبة. بعد إزالة العائق نتحقق من سريان الماء ونوضح الملاحظات التي قد تشير إلى تراكم متكرر أو خلل في الميل أو التوصيل، بدل الاكتفاء بفتح مؤقت للمجرى.",
         includes=["فحص الأحواض والسيفونات والبالوعات", "تحديد ما إذا كان الانسداد في نقطة واحدة أو أكثر", "إزالة العائق بحسب طبيعة خط الصرف", "اختبار التصريف بعد الانتهاء"],
         cases=["بطء تصريف حوض المطبخ", "تجمع المياه في أرضية الحمام", "عودة انسداد البالوعة بعد فترة قصيرة"]),
    dict(slug="bathroom-kitchen-plumbing", category="plumbing", icon="faucet", title="صيانة سباكة الحمامات والمطابخ", short="إصلاح الخلاطات والسيفونات والمراحيض والتوصيلات اليومية في المنزل.",
         intro="أعطال السباكة الصغيرة قد تتحول إلى هدر ماء أو تلف في الأثاث إذا تأخر التعامل معها. تشمل صيانة سباكة الحمامات والمطابخ بالرياض فحص الخلاطات والمغاسل والمراحيض والسيفونات والتوصيلات الظاهرة، ثم معالجة الجزء المتأثر بدل تغيير مكونات سليمة بلا حاجة.",
         detail="نراجع مصدر التنقيط أو ضعف التدفق أو الرائحة، ونميّز بين مشكلة في القطعة نفسها ومشكلة في التوصيل أو صرف المياه. قد يتطلب العمل تبديل جلدة أو محبس أو سيفون، أو إعادة تركيب خلاط أو إصلاح تسرب أسفل المغسلة. يتم اختيار القطعة المناسبة وفق المقاس والحالة بعد الاطلاع على الموقع، ويمكن للعميل إرسال صورة واضحة على واتساب قبل التنسيق للزيارة.",
         includes=["فحص وإصلاح الخلاطات والمحابس", "صيانة سيفونات الأحواض والمراحيض", "معالجة تنقيط التوصيلات الظاهرة", "تركيب أو استبدال القطع المتضررة حسب الحاجة"],
         cases=["تسريب أسفل حوض المطبخ", "خلاط لا يغلق بإحكام", "مشكلة في شطف المرحاض أو صرف المغسلة"]),
    dict(slug="water-heaters", category="plumbing", icon="heater", title="تركيب وصيانة سخانات المياه", short="تركيب السخان وفحص توصيلات الماء والكهرباء ومعالجة الأعطال الشائعة.",
         intro="السخان يجمع بين توصيلات المياه والكهرباء، ولهذا يحتاج تركيبه أو صيانته إلى اهتمام بالوصلات والسلامة معًا. نقدم في الرياض خدمة تركيب وصيانة سخانات المياه المنزلية، وفحص أسباب ضعف الماء الساخن أو التنقيط حول الجهاز قبل تحديد الإجراء المناسب.",
         detail="يتضمن الفحص حالة محابس الدخول والخروج، والوصلات الظاهرة، ومكان التثبيت، والتوصيل الكهربائي ضمن نطاق العمل. إذا كان السخان قديمًا أو تالفًا نوضح ما إذا كانت الصيانة مجدية أو أن الاستبدال أنسب، مع ترك اختيار الجهاز والقطعة للعميل بعد توضيح المتطلبات. عند وجود رائحة احتراق أو تماس أو تسرب واضح، يُنصح بفصل التغذية عن الجهاز وتجنب تشغيله حتى يفحصه مختص.",
         includes=["تركيب سخانات المياه المنزلية", "فحص التوصيلات والمحابس المحيطة", "معالجة التنقيط أو ضعف التسخين بعد التشخيص", "مراجعة التشغيل بعد الصيانة"],
         cases=["سخان جديد يحتاج تركيبًا", "تنقيط حول السخان", "المياه لا تسخن كما ينبغي"]),
    dict(slug="pumps-tanks", category="plumbing", icon="pump", title="صيانة مضخات وخزانات المياه", short="فحص ضعف ضغط المياه وتوصيلات المضخة والخزان والعوامة.",
         intro="ضعف تدفق المياه أو تشغيل المضخة بصورة متقطعة لا يعني دائمًا تلف المضخة نفسها؛ فقد يرتبط بمحبس أو عوامة أو تسرب في التوصيلات. توفر خدمة مضخات وخزانات المياه بالرياض فحصًا أوليًا لمسار التغذية والضغط والوصلات المحيطة لتحديد سبب المشكلة الأقرب.",
         detail="يشمل نطاق العمل مراجعة التوصيلات الظاهرة للمضخة والخزان، وفحص المؤشرات التي تظهر عند التشغيل، ثم تحديد القطعة أو الإجراء المطلوب. قد يكون الحل تنظيفًا أو ضبطًا أو استبدال جزء تالف أو تعديل توصيل، وفق النتيجة الفعلية للفحص. نوضح للعميل ما يلزم قبل التنفيذ، ولا ننسب ضعف الضغط تلقائيًا إلى عنصر واحد من غير تشخيص.",
         includes=["فحص أعراض ضعف ضغط المياه", "مراجعة وصلات المضخة والخزان", "فحص العوامة والمحابس المرتبطة", "صيانة أو تركيب القطع بحسب الحالة"],
         cases=["ضعف الماء في أكثر من نقطة", "توقف المضخة أو تكرر تشغيلها", "تسرب حول توصيلات الخزان"]),
    dict(slug="water-pipe-installation", category="plumbing", icon="layers", title="تمديد وتأسيس مواسير المياه", short="تجهيز وتمديد خطوط المياه المنزلية وتعديل التوصيلات عند التجديد.",
         intro="التأسيس الجيد يجعل استخدام المطابخ والحمامات أسهل ويساعد على الوصول إلى التوصيلات عند الصيانة. تشمل خدمة تمديد مواسير المياه في الرياض إنشاء خطوط تغذية للتركيبات الجديدة أو تعديل التوصيلات القائمة أثناء تجديد الحمام أو المطبخ.",
         detail="نبدأ بمراجعة نقاط الاستخدام المطلوبة ومواقع الأجهزة والخلاطات والمحابس، ثم نحدد مسار التمديد والقطع المناسبة بحسب طبيعة المكان. في أعمال التجديد، نهتم بفهم وضع الشبكة الحالية قبل توصيل الخطوط الجديدة بها. تختلف المواد والمقاسات وطريقة التنفيذ من مشروع لآخر؛ لذلك تُحدَّد التفاصيل الفنية والكميات بعد معاينة فعلية، مع اختبار التوصيلات قبل الإغلاق النهائي حيث تسمح مراحل العمل.",
         includes=["تحديد نقاط التغذية المطلوبة", "تمديد أو تعديل خطوط المياه", "تجهيز وصلات الخلاطات والأجهزة", "فحص التوصيلات بعد التركيب"],
         cases=["تجديد مطبخ أو حمام", "إضافة نقطة ماء لجهاز جديد", "تعديل مسار أنبوب ظاهر أو قائم"]),
    dict(slug="electrical-faults", category="electrical", icon="bolt", title="إصلاح الأعطال الكهربائية والقواطع", short="فحص أسباب فصل القاطع وانقطاع بعض الدوائر ومشكلات الأحمال والتوصيلات.",
         intro="القاطع الذي يفصل باستمرار علامة تستحق التشخيص، لا مجرد إعادة تشغيل متكررة. نقدم خدمة فحص وإصلاح الأعطال الكهربائية في الرياض لتحديد الدائرة المتأثرة ومراجعة القواطع والتوصيلات الظاهرة والأجهزة المرتبطة بالعطل قبل تنفيذ الإصلاح المناسب.",
         detail="قد يكون السبب حملًا زائدًا، أو تلفًا في مفتاح أو فيش، أو وصلة غير محكمة، أو خللًا في جهاز موصول بالدائرة. يبدأ الفحص بسؤال العميل عن وقت ظهور المشكلة وما الذي كان يعمل وقتها، ثم مراجعة الجزء المتأثر بصورة آمنة. في حال ظهور شرر أو رائحة احتراق أو سخونة واضحة، ينبغي إيقاف استخدام الدائرة وترك الفحص لفني مختص. لا نعرض حلولًا شكلية تتجاوز سبب العطل من دون تشخيص.",
         includes=["فحص أسباب فصل القواطع المتكرر", "مراجعة الدوائر والتوصيلات المتأثرة", "استبدال القاطع أو القطعة التالفة عند الحاجة", "التحقق من عودة التشغيل بعد المعالجة"],
         cases=["انقطاع الكهرباء عن غرفة أو جزء من المنزل", "قاطع يفصل عند تشغيل جهاز", "سخونة أو رائحة غير معتادة من نقطة كهرباء"]),
    dict(slug="electrical-wiring", category="electrical", icon="circuit", title="تأسيس وتمديد الكهرباء", short="تمديد نقاط كهربائية جديدة وتنظيم مسارات الأسلاك في التجديد والتجهيز.",
         intro="عند تجديد منزل أو إضافة أجهزة جديدة، تحتاج النقاط الكهربائية إلى توزيع يراعي الاستخدام الفعلي للمكان. تشمل خدمة تأسيس وتمديد الكهرباء بالرياض تجهيز أو تعديل مسارات الأسلاك والمفاتيح والأفياش والإنارة حسب مخطط العمل وحالة التمديدات الموجودة.",
         detail="نراجع احتياجات الغرف والأجهزة ومواقع الأثاث قبل تحديد النقاط المطلوبة، ثم نوضح مسار التمديد وطريقة التنفيذ المناسبة للموقع. في الشبكات القائمة، يجب معرفة سعة الدائرة وحالة الأسلاك قبل إضافة أحمال جديدة. هذه الخدمة مناسبة لتجهيز غرفة أو تعديل مطبخ أو إعادة توزيع نقاط الكهرباء أثناء أعمال التشطيب، مع اختبار النقاط التي جرى تركيبها قبل التسليم.",
         includes=["تحديد مواقع النقاط الكهربائية", "تمديد الأسلاك والمواسير بحسب حالة الموقع", "تركيب علب ومفاتيح وأفياش", "فحص النقاط بعد التوصيل"],
         cases=["تجهيز غرفة جديدة", "إضافة نقطة لجهاز منزلي", "إعادة توزيع الأفياش أثناء التجديد"]),
    dict(slug="switches-outlets", category="electrical", icon="socket", title="تركيب الأفياش والمفاتيح", short="تركيب واستبدال الأفياش والمفاتيح ومعالجة الارتخاء والسخونة.",
         intro="الفيش المرتخي أو المفتاح الذي يصدر صوتًا عند التشغيل قد يكون مؤشرًا على وصلة غير سليمة. نقدم خدمة تركيب وصيانة الأفياش والمفاتيح بالرياض، سواء لإضافة نقطة جديدة ضمن تمديد مناسب أو لاستبدال قطعة تالفة بعد فحص السبب.",
         detail="يشمل العمل مراجعة مكان التركيب وحالة الأسلاك والعلبة، واختيار قطعة مناسبة لنوع الاستخدام والحمل المتصل بها. عند ظهور سخونة أو تغير لون أو رائحة، لا يكفي تغيير الغطاء الخارجي؛ بل يجب فحص التوصيل والدائرة المحيطة. نوضح للعميل إن كانت المشكلة في القطعة أو في الشبكة قبل تنفيذ الاستبدال، ثم نتحقق من ثباتها وتشغيلها بعد التركيب.",
         includes=["تركيب أو استبدال الأفياش والمفاتيح", "فحص العلب والوصلات الظاهرة", "معالجة الارتخاء أو ضعف التلامس حسب الحالة", "اختبار التشغيل بعد التركيب"],
         cases=["فيش تالف أو مرتخٍ", "مفتاح لا يعمل بانتظام", "إضافة نقطة كهرباء في مكان مناسب"]),
    dict(slug="lighting-installation", category="electrical", icon="light", title="تركيب الإنارة والثريات والسبوت لايت", short="تجهيز وتركيب وحدات الإنارة المنزلية مع مراعاة التوزيع والتوصيل الآمن.",
         intro="الإنارة تغيّر إحساس الغرفة واستخدامها اليومي. نقدم خدمة تركيب الإنارة بالرياض، من وحدات السقف والثريات إلى السبوت لايت والشرائط الضوئية، مع الاهتمام بملاءمة موقع التركيب للتوصيل الكهربائي والسطح الحامل.",
         detail="نناقش نوع الوحدة ومكانها وارتفاع السقف وطريقة التحكم المطلوبة قبل التركيب. قد تحتاج الثريا إلى تثبيت مختلف عن السبوت لايت، وقد تتطلب الإضاءة المخفية تجهيزًا مسبقًا لمسار الأسلاك ومصدر الطاقة. نراعي فصل التيار أثناء التنفيذ وفحص نقطة التغذية ثم تجربة التشغيل، مع توضيح أي أعمال إضافية مطلوبة قبل البدء. يمكن إرسال صورة للوحدة والموقع عبر واتساب لتسهيل تحديد الاحتياج.",
         includes=["تركيب وحدات السقف والثريات", "تركيب سبوت لايت وإضاءة LED", "فحص نقطة الكهرباء ومكان التثبيت", "اختبار التشغيل بعد التركيب"],
         cases=["ثريا جديدة لغرفة المعيشة", "سبوت لايت لممر أو غرفة", "تحديث إنارة قديمة إلى LED"]),
    dict(slug="lighting-maintenance", category="electrical", icon="sun", title="صيانة الإنارة وإصلاح أعطالها", short="تشخيص الوميض والانقطاع وتبديل الوحدات أو التوصيلات المتضررة.",
         intro="إذا كانت اللمبة تومض أو تنطفئ بعض وحدات الإنارة من وقت لآخر، فالمشكلة قد تكون في المصباح أو المشغل أو المفتاح أو التوصيل. تشمل صيانة الإنارة بالرياض فحص العنصر المتأثر وتحديد سبب الخلل قبل اقتراح الاستبدال أو الإصلاح.",
         detail="نراجع توقيت ظهور المشكلة وعدد الوحدات المتأثرة، ثم نفحص نقطة التشغيل والمفتاح والوحدة بحسب نوعها. في إنارة LED قد يختلف سبب العطل عن الإنارة التقليدية، لذا يساعد معرفة نوع المصباح والمشغل على تحديد القطعة المناسبة. بعد المعالجة نجرب التشغيل ونتأكد من ثبات الإضاءة. إذا كان العطل مصحوبًا بسخونة أو رائحة احتراق، يُفضّل إيقاف الدائرة حتى الفحص.",
         includes=["تشخيص وميض الإنارة أو انقطاعها", "فحص المفاتيح والوحدات والمشغلات", "استبدال الجزء التالف بحسب الحالة", "التحقق من انتظام التشغيل"],
         cases=["وميض متكرر في السبوت لايت", "تعطل جزء من إضاءة الغرفة", "توقف وحدة LED عن العمل"]),
]

CATEGORIES = {
    "plumbing": ("خدمات السباكة", "حلول لتمديدات المياه والصرف والتجهيزات المنزلية.", "سباك بالرياض"),
    "electrical": ("خدمات الكهرباء والإنارة", "من فحص العطل إلى تركيب النقاط والإنارة المناسبة.", "كهربائي بالرياض"),
}

ICON_PATHS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.79 19.79 0 0 1 3.09 5.18 2 2 0 0 1 5.08 3h3a2 2 0 0 1 2 1.72c.12.96.35 1.91.69 2.81a2 2 0 0 1-.45 2.11L9.05 10.91a16 16 0 0 0 4.04 4.04l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.69A2 2 0 0 1 22 16.92Z"/>',
    "arrow": '<path d="m5 12 14 0m-6-6 6 6-6 6"/>',
    "chevron": '<path d="m9 18 6-6-6-6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "check": '<path d="m5 12 4 4L19 6"/>',
    "pin": '<path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    "drop": '<path d="M12 22a8 8 0 0 0 8-8c0-4.6-8-12-8-12S4 9.4 4 14a8 8 0 0 0 8 8Z"/><path d="M8 15a4 4 0 0 0 4 4"/>',
    "pipe": '<path d="M4 4v6a4 4 0 0 0 4 4h8a4 4 0 0 1 4 4v2M1 4h6m10 16h6"/><circle cx="12" cy="14" r="1"/>',
    "faucet": '<path d="M4 21v-8a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v2h-6v-2H8v8M8 5h8M12 5v4M18 19v2"/>',
    "heater": '<rect x="7" y="2" width="10" height="16" rx="3"/><path d="M10 18v4m4-4v4M10 6h4M11 13h2"/>',
    "pump": '<rect x="5" y="7" width="13" height="11" rx="2"/><path d="M2 11h3m13 0h4m-17 7v3m10-3v3M9 7V4h5v3"/><circle cx="11.5" cy="12.5" r="2"/>',
    "layers": '<path d="m12 2 9 5-9 5-9-5 9-5Zm-9 10 9 5 9-5M3 17l9 5 9-5"/>',
    "bolt": '<path d="m13 2-9 12h7l-1 8 10-12h-7l0-8Z"/>',
    "circuit": '<path d="M3 7h5l3 5h4l3-5h3M3 17h5l3-5M15 12l3 5h3"/><circle cx="3" cy="7" r="1"/><circle cx="21" cy="7" r="1"/><circle cx="3" cy="17" r="1"/><circle cx="21" cy="17" r="1"/>',
    "socket": '<rect x="4" y="2" width="16" height="20" rx="3"/><path d="M9 8v3m6-3v3m-5 6h4"/>',
    "light": '<path d="M9 18h6m-5 3h4M9 15c-.2-2-3-3.4-3-7a6 6 0 0 1 12 0c0 3.6-2.8 5-3 7H9Z"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4m0-14.2-1.4 1.4M6.3 17.7l-1.4 1.4"/>',
}

def esc(text: str) -> str:
    return html.escape(text, quote=True)

def icon(name: str, size=24, klass="") -> str:
    return f'<svg class="{klass}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON_PATHS[name]}</svg>'

def wa_icon(size=24):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="/assets/whatsapp.svg#wa"/></svg>'

def wa_url(message="مرحبًا أبو محمد، أرغب في الاستفسار عن خدمة داخل الرياض."):
    from urllib.parse import quote
    return WA + "?text=" + quote(message, safe="")

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c") + '</script>'

def canonical(path):
    return SITE + path

def asset_url(path):
    asset = OUT / path.lstrip("/")
    version = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
    return f"{path}?v={version}"

def breadcrumbs(items):
    return '<nav class="breadcrumbs container" aria-label="مسار التنقل"><a href="/">الرئيسية</a>' + ''.join(icon("chevron", 15) + (f'<a href="{esc(url)}">{esc(label)}</a>' if url else f'<span aria-current="page">{esc(label)}</span>') for label, url in items) + '</nav>'

def breadcrumb_schema(items):
    chain = [("الرئيسية", "/")] + items
    return {"@type":"BreadcrumbList","@id":canonical(items[-1][1] or "/")+"#breadcrumbs","itemListElement":[{"@type":"ListItem","position":n+1,"name":label,"item":canonical(path) if path else canonical(items[-1][1] or "/")} for n,(label,path) in enumerate(chain)]}

def service_area_schema():
    return {"@type": "City", "name": CITY,
            "containedInPlace": {"@type": "Country", "name": "المملكة العربية السعودية"}}

def business_schema():
    return {
        "@type": ["Plumber", "Electrician"],
        "@id": SITE + "/#business",
        "name": NAME,
        "url": SITE + "/",
        "telephone": E164,
        "image": SITE + "/assets/team.webp",
        "logo": SITE + "/assets/icon-180.png",
        "description": "خدمات السباكة والكهرباء والإنارة في مواقع العملاء داخل الرياض، بإدارة من حي المصيف. " + SERVICE_MODE,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": CITY,
            "addressRegion": "منطقة الرياض",
            "addressCountry": "SA",
        },
        "areaServed": service_area_schema(),
        "contactPoint": {
            "@type": "ContactPoint", "telephone": E164,
            "contactType": "طلب خدمات السباكة والكهرباء", "availableLanguage": "ar",
            "areaServed": service_area_schema(), "url": canonical("/contact/"),
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "خدمات السباكة والكهرباء في الرياض",
            "itemListElement": [
                {"@type": "OfferCatalog", "name": CATEGORIES[c][0], "itemListElement": [
                    {"@type": "Offer", "itemOffered": {
                        "@type": "Service", "@id": canonical("/services/" + s["slug"] + "/") + "#service",
                        "name": s["title"], "serviceType": s["title"],
                        "url": canonical("/services/" + s["slug"] + "/"),
                        "provider": {"@id": SITE + "/#business"}, "areaServed": service_area_schema(),
                    }} for s in SERVICES if s["category"] == c
                ]} for c in CATEGORIES
            ],
        },
    }

def business_details():
    return f'''<section class="business-details" id="business-details" aria-labelledby="business-details-title">
    <div class="business-details-heading"><span class="panel-icon">{icon('pin',28)}</span><div><span class="eyebrow">بيانات النشاط وطريقة تقديم الخدمة</span><h2 id="business-details-title">{esc(NAME)}</h2><p>خدمات سباكة وكهرباء وإنارة في موقع العميل داخل الرياض.</p></div></div>
    <dl class="business-facts"><div><dt>الاتصال وواتساب</dt><dd><a href="tel:{PHONE}"><bdi dir="ltr">{PHONE}</bdi></a></dd></div><div><dt>نطاق الخدمة</dt><dd>مدينة الرياض، المملكة العربية السعودية</dd></div><div><dt>منطقة إدارة النشاط</dt><dd>{esc(BASE_AREA)}</dd></div><div><dt>طريقة تقديم الخدمة</dt><dd>زيارة موقع العميل بعد التنسيق</dd></div></dl>
    <p class="business-service-mode">{icon('check',20)}<span>{SERVICE_MODE}</span></p>
    <a class="business-map-link" href="{wa_url()}" target="_blank" rel="noopener noreferrer">نسّق زيارة عبر واتساب {icon('arrow',17)}</a>
    </section>'''

def footer_address():
    return f'''<div class="footer-address"><strong>منطقة الإدارة · دون استقبال العملاء</strong><span>{esc(BASE_AREA)}</span><span>تنفيذ الخدمات في موقع العميل داخل الرياض.</span></div>'''

def head(title, description, path, extra_schema=None):
    url=canonical(path)
    verification_tag = f'<meta name="google-site-verification" content="{esc(GOOGLE_SITE_VERIFICATION)}">' if path == "/" else ""
    page_type = {"/about/": "AboutPage", "/contact/": "ContactPage"}.get(path, "WebPage")
    page_schema = {"@type":page_type,"@id":url+"#webpage","url":url,"name":title,"description":description,"inLanguage":"ar-SA","isPartOf":{"@id":SITE+"/#website"},"about":{"@id":SITE+"/#business"},"dateModified":LAST_UPDATED}
    if path.startswith("/services/") and path != "/services/":
        page_schema["mainEntity"] = {"@id": url + "#service"}
    elif path in ("/about/", "/contact/"):
        page_schema["mainEntity"] = {"@id": SITE + "/#business"}
    graph=[business_schema(), {"@type":"WebSite","@id":SITE+"/#website","name":NAME,"url":SITE+"/","inLanguage":"ar-SA","publisher":{"@id":SITE+"/#business"}}, page_schema]
    if extra_schema: graph.extend(extra_schema if isinstance(extra_schema,list) else [extra_schema])
    return f'''<!doctype html><html lang="ar" dir="rtl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#10282b"><meta name="color-scheme" content="light">{verification_tag}
<title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{esc(url)}"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/assets/icon-32.png"><link rel="apple-touch-icon" href="/assets/icon-180.png">
<meta property="og:type" content="website"><meta property="og:locale" content="ar_SA"><meta property="og:site_name" content="{NAME}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{esc(url)}"><meta property="og:image" content="{SITE}/assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="{asset_url('/assets/style.css')}">{jsonld({'@context':'https://schema.org','@graph':graph})}</head><body><a class="skip" href="#main">انتقل إلى المحتوى</a>'''

def header():
    return f'''<header class="site-header"><div class="container header-inner"><a class="brand" href="/" aria-label="{NAME}، الرئيسية"><img src="/assets/icon-180.png" width="48" height="48" alt="" fetchpriority="high"><span><strong>أبو محمد</strong><small>سباك وكهربائي · الرياض</small></span></a>
    <nav class="desktop-nav" aria-label="القائمة الرئيسية"><a href="/">الرئيسية</a><a href="/services/">كل الخدمات</a><a href="/plumbing/">السباكة</a><a href="/electrical/">الكهرباء والإنارة</a><a href="/about/">من نحن</a><a href="/contact/">تواصل معنا</a></nav>
    <a class="header-call" href="tel:{PHONE}">{icon('phone',18)}<span>اتصل الآن</span></a>
    <details class="mobile-menu"><summary aria-label="فتح القائمة">{icon('menu',25)}</summary><nav aria-label="قائمة الجوال"><a href="/">الرئيسية</a><a href="/services/">كل الخدمات</a><a href="/plumbing/">السباكة</a><a href="/electrical/">الكهرباء والإنارة</a><a href="/about/">من نحن</a><a href="/contact/">تواصل معنا</a></nav></details></div></header>'''

def footer():
    plist=''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s["title"])}</a></li>' for s in SERVICES[:6])
    elist=''.join(f'<li><a href="/services/{s["slug"]}/">{esc(s["title"])}</a></li>' for s in SERVICES[6:])
    return f'''<footer class="footer"><div class="container"><div class="footer-grid"><div class="footer-about"><a class="brand brand-footer" href="/"><img src="/assets/icon-180.png" width="52" height="52" alt=""><span><strong>أبو محمد</strong><small>سباك وكهربائي · الرياض</small></span></a><p>سباكة، كهرباء وإنارة للمنازل داخل مدينة الرياض. أرسل تفاصيل المشكلة أو اتصل للتنسيق على الخدمة المناسبة.</p><span class="footer-location">{icon('pin',18)} نطاق الخدمة: مدينة الرياض</span>{footer_address()}</div><div><h2>السباكة</h2><ul>{plist}</ul></div><div><h2>الكهرباء والإنارة</h2><ul>{elist}</ul></div><div><h2>روابط وتواصل</h2><ul><li><a href="/services/">جميع الخدمات</a></li><li><a href="/about/">من نحن</a></li><li><a href="/contact/">تواصل معنا</a></li><li><a href="tel:{PHONE}" dir="ltr">{PHONE}</a></li></ul></div></div><div class="footer-bottom"><span>© 2026 {NAME}</span><div class="credit"><span>Designed &amp; developed by <a href="https://www.eslam-elshikh.com/" target="_blank" rel="noopener noreferrer">Eng. Eslam Elshikh</a></span><a href="https://www.eslam-elshikh.com/" target="_blank" rel="noopener noreferrer">المهندس إسلام الشيخ</a></div></div></div></footer>
    <aside class="floating-contact" aria-label="تواصل سريع"><a class="float-wa" href="{wa_url()}" target="_blank" rel="noopener noreferrer" aria-label="راسل أبو محمد على واتساب"><svg width="27" height="27" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="/assets/whatsapp.svg#wa"/></svg><span class="float-label">واتساب</span></a><a class="float-phone" href="tel:{PHONE}" aria-label="اتصل بأبو محمد على {PHONE}">{icon('phone',25)}<span class="float-label">اتصل الآن</span></a></aside>
    <script src="{asset_url('/assets/site.js')}" defer></script></body></html>'''

def ctas(service=None, inverse=False):
    msg = f"مرحبًا أبو محمد، أرغب في خدمة {service} داخل الرياض. الحي: ... وتفاصيل الطلب: ..." if service else "مرحبًا أبو محمد، أرغب في طلب خدمة سباكة أو كهرباء داخل الرياض. الحي: ... وتفاصيل الطلب: ..."
    return f'<div class="actions"><a class="btn btn-primary" href="{wa_url(msg)}" target="_blank" rel="noopener noreferrer"><svg width="21" height="21" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="/assets/whatsapp.svg#wa"/></svg>راسلنا على واتساب</a><a class="btn btn-outline {"on-dark" if inverse else ""}" href="tel:{PHONE}">{icon("phone",19)} اتصل الآن</a></div>'

def service_card(s):
    category="سباكة" if s["category"]=="plumbing" else "كهرباء وإنارة"
    return f'''<a class="service-card {s['category']}" href="/services/{s['slug']}/"><span class="card-top"><span class="service-icon">{icon(s['icon'],30)}</span><span class="card-category">{category}</span></span><span class="card-content"><strong>{esc(s['title'])}</strong><span>{esc(s['short'])}</span></span><span class="card-link">تفاصيل الخدمة {icon('arrow',18)}</span></a>'''

def contact_band():
    return f'''<section class="contact-band"><div class="container band-inner"><div><span class="eyebrow light">تواصل مباشر</span><h2>عندك عطل سباكة أو كهرباء؟</h2><p>أرسل نوع المشكلة وحيّك داخل الرياض، ونسّق معنا الخطوة المناسبة.</p></div>{ctas(inverse=True)}</div></section>'''

def section_heading(eyebrow,title,subtitle=""):
    return f'<div class="section-heading"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{f"<p>{subtitle}</p>" if subtitle else ""}</div>'

def home():
    title="أبو محمد سباك وكهربائي بالرياض | سباكة وكهرباء وإنارة"
    desc=f"{NAME} لخدمات السباكة والكهرباء والإنارة في مواقع العملاء داخل الرياض. إدارة النشاط من حي المصيف دون استقبال العملاء. اتصال وواتساب: {PHONE}."
    featured=[SERVICES[i] for i in [0,1,2,3,6,7,8,9]]
    cards=''.join(service_card(s) for s in featured)
    faq=[("ما نطاق خدمة أبو محمد؟","نخدم العملاء داخل مدينة الرياض. أرسل اسم الحي وطبيعة الطلب عبر واتساب لتنسيق التفاصيل."),("هل تستقبلون العملاء في مقر الإدارة؟",SERVICE_MODE),("هل يمكن إرسال صورة للعطل قبل الزيارة؟","نعم، يمكنك إرسال صورة أو شرح مختصر للمشكلة والحي عبر واتساب حتى تتضح الخدمة المطلوبة."),("هل يشمل العمل السباكة والكهرباء؟","نعم، يقدم أبو محمد خدمات سباكة وكهرباء وإنارة؛ وتشمل الأعمال الموضحة في صفحات الخدمات أعمال الإصلاح والصيانة والتركيب بحسب الحالة."),("كيف تُحدد تكلفة الخدمة؟","تختلف التكلفة بحسب نوع العمل والقطع المطلوبة وحالة الموقع، ويمكن مناقشة التفاصيل بعد وصف المشكلة أو معاينتها.")]
    faq_html=''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in faq)
    content=f'''<main id="main"><section class="hero"><div class="container hero-grid"><div class="hero-copy"><span class="eyebrow hero-eyebrow"><span class="dot"></span> خدمة داخل مدينة الرياض</span><h1>أبو محمد سباك وكهربائي بالرياض.<br><em>سباكة وإنارة</em> تريح بالك.</h1><p class="hero-lead">مع أبو محمد، اطلب خدمة السباكة أو الكهرباء اللي تحتاجها في منزلك: من تسربات المياه والصرف والسخانات إلى الأعطال الكهربائية وتركيب الإنارة.</p>{ctas()}<div class="hero-micro">{icon('pin',17)} نخدم داخل الرياض <span aria-hidden="true">·</span> <span dir="ltr">{PHONE}</span></div></div><div class="hero-visual"><div class="hero-orbit orbit-one"></div><div class="hero-orbit orbit-two"></div><div class="hero-pill pill-water">{icon('drop',18)} سباكة</div><div class="hero-pill pill-power">{icon('bolt',18)} كهرباء</div><img src="/assets/team.webp" width="760" height="760" alt="أفاتار ثلاثي الأبعاد لسباك وكهربائي يمثلان خدمات أبو محمد" fetchpriority="high"></div></div><div class="hero-bottom container"><span>صيانة وتركيب حسب احتياج منزلك</span><a href="#services">تعرّف على الخدمات <span aria-hidden="true">↓</span></a></div></section>
    <section class="section intro-section"><div class="container intro-grid"><div>{section_heading('ماذا نقدم؟','خدمات البيت من الماء إلى النور','نبدأ بفهم المشكلة ثم نحدد الخدمة المناسبة لها. اختر نوع العمل واطّلع على تفاصيله قبل التواصل.')}</div><div class="intro-side"><a class="category-tile tile-water" href="/plumbing/"><span class="category-symbol">{icon('drop',36)}</span><span><strong>خدمات السباكة</strong><small>المياه · الصرف · السخانات</small></span>{icon('arrow',20)}</a><a class="category-tile tile-power" href="/electrical/"><span class="category-symbol">{icon('bolt',36)}</span><span><strong>الكهرباء والإنارة</strong><small>الأعطال · التمديدات · الإضاءة</small></span>{icon('arrow',20)}</a></div></div></section>
    <section class="section services-section" id="services"><div class="container">{section_heading('الخدمات الأكثر طلبًا','اختر الخدمة المناسبة','كل بطاقة تفتح صفحة مستقلة فيها نطاق العمل والحالات المناسبة وطريقة طلب الخدمة.')}<div class="cards-grid">{cards}</div><a class="text-link" href="/services/">استعرض جميع الخدمات {icon('arrow',19)}</a></div></section>
    <section class="section process-section"><div class="container process-grid"><div>{section_heading('من أول رسالة إلى التنفيذ','خطوات واضحة من البداية')}<p>صف العطل وموقعه داخل الرياض. تساعدنا صورة أو تفاصيل بسيطة على فهم طلبك، ثم نتفق على خطوات المعاينة أو العمل المناسب بحسب الحالة.</p>{ctas()}</div><ol class="process-list"><li><span>01</span><div><strong>أرسل التفاصيل</strong><p>نوع المشكلة، الحي، وصورة إن توفرت.</p></div></li><li><span>02</span><div><strong>نحدد المطلوب</strong><p>نوضح نطاق الخدمة والاحتياجات قبل البدء.</p></div></li><li><span>03</span><div><strong>تنفيذ وفحص</strong><p>تنفيذ العمل ثم مراجعة التشغيل في الجزء المعالج.</p></div></li></ol></div></section>
    <section class="section business-section"><div class="container">{business_details()}</div></section>
    <section class="section faq-section"><div class="container faq-grid"><div>{section_heading('أسئلة شائعة','إجابات قبل ما تتواصل')}<p>إذا احتجت تفاصيل عن حالتك تحديدًا، أرسل لنا وصفًا مختصرًا على واتساب.</p></div><div class="faq-list">{faq_html}</div></div></section>{contact_band()}</main>'''
    return head(title,desc,"/")+header()+content+footer()

def service_page(s):
    cat=CATEGORIES[s['category']]
    path=f"/services/{s['slug']}/"
    title=f"{s['title']} بالرياض | {NAME}"
    desc=f"{s['intro'][:145].rstrip(' ،.')}... تواصل مع أبو محمد على {PHONE} لطلب الخدمة داخل الرياض."
    related=[r for r in SERVICES if r['category']==s['category'] and r['slug']!=s['slug']][:3]
    related_cards=''.join(service_card(r) for r in related)
    faq_q=f"هل تتوفر خدمة {s['title']} داخل الرياض؟"
    faq_a=f"نعم، يمكن طلب {s['title']} داخل مدينة الرياض. أرسل اسم الحي وتفاصيل الحالة للتنسيق."
    content=f'''<main id="main">{breadcrumbs([('كل الخدمات','/services/'),(s['title'],None)])}<section class="inner-hero"><div class="container inner-grid"><div><span class="eyebrow">{cat[0]} · مدينة الرياض</span><h1>{esc(s['title'])} <span>بالرياض</span></h1><p>{esc(s['intro'])}</p>{ctas(s['title'])}</div><div class="inner-art {s['category']}"><span class="inner-art-circle">{icon(s['icon'],105)}</span><span class="art-caption">{cat[2]}</span></div></div></section>
    <section class="section content-section"><div class="container content-grid"><article><span class="eyebrow">تفاصيل الخدمة</span><h2>حل يناسب حالة الموقع</h2><p>{esc(s['detail'])}</p><h2>متى تطلب هذه الخدمة؟</h2><p>إذا لاحظت إحدى الحالات التالية، يساعد وصف المشكلة والصور المتاحة على فهم الاحتياج قبل تحديد العمل المناسب:</p><ul class="case-list">{''.join(f'<li>{icon("check",18)} {esc(c)}</li>' for c in s['cases'])}</ul><h2>ما الذي تشمل عليه الخدمة؟</h2><div class="scope-grid">{''.join(f'<div>{icon("check",20)}<span>{esc(a)}</span></div>' for a in s['includes'])}</div><p class="note">تختلف تفاصيل التنفيذ والقطع المطلوبة بحسب الحالة الفعلية في الموقع. نناقش نطاق العمل المناسب قبل البدء.</p></article><aside class="side-panel"><span class="side-icon">{icon(s['icon'],33)}</span><h2>تحتاج {esc(s['title'])}؟</h2><p>أرسل شرحًا مختصرًا للعطل واسم الحي في الرياض، أو اتصل مباشرة.</p>{ctas(s['title'])}<small>{icon('pin',16)} نطاق الخدمة: مدينة الرياض</small></aside></div></section>
    <section class="section related-section"><div class="container">{section_heading('قد يفيدك أيضًا','خدمات مرتبطة')}<div class="cards-grid related-grid">{related_cards}</div><a class="text-link" href="/{s['category']}/">كل {cat[0]} {icon('arrow',19)}</a></div></section>{contact_band()}</main>'''
    schema=[breadcrumb_schema([('كل الخدمات','/services/'),(s['title'],path)]),{"@type":"Service","@id":canonical(path)+"#service","name":s['title'],"description":s['intro'],"serviceType":s['title'],"areaServed":service_area_schema(),"provider":{"@id":SITE+"/#business"},"url":canonical(path)}]
    return head(title,desc,path,schema)+header()+content+footer()

def listing_page(category=None):
    if category:
        name,sub,term=CATEGORIES[category]; path=f"/{category}/"; chosen=[s for s in SERVICES if s['category']==category]
        title=f"{name} بالرياض | {NAME}"; desc=f"{name} في مدينة الرياض من أبو محمد: {', '.join(s['title'] for s in chosen[:4])}. تواصل على {PHONE} لمعرفة الخدمة المناسبة."
        crumb=breadcrumbs([(name,None)]); related=f'<a class="text-link" href="/{"electrical" if category=="plumbing" else "plumbing"}/">شاهد {CATEGORIES["electrical" if category=="plumbing" else "plumbing"][0]} {icon("arrow",19)}</a>'
    else:
        name="جميع خدمات السباكة والكهرباء"; sub="خدمات منظمة لكل احتياج في منزلك داخل الرياض."; term="خدمات سباكة وكهرباء بالرياض"; path="/services/"; chosen=SERVICES
        title=f"خدمات السباكة والكهرباء والإنارة بالرياض | {NAME}"; desc=f"تصفح خدمات {NAME} في الرياض: كشف وإصلاح التسربات، الصرف، السخانات، المضخات، تمديدات الكهرباء، الأفياش والإنارة. اتصال وواتساب {PHONE}."
        crumb=breadcrumbs([("كل الخدمات",None)]); related=''
    cards=''.join(service_card(s) for s in chosen)
    content=f'''<main id="main">{crumb}<section class="listing-hero"><div class="container"><span class="eyebrow">{term} · مدينة الرياض</span><h1>{name} <span>بالرياض</span></h1><p>{sub} استعرض كل خدمة في صفحتها المستقلة، ثم أرسل لنا تفاصيل طلبك والحي للتنسيق.</p>{ctas()}</div></section><section class="section services-section"><div class="container">{section_heading('اختر احتياجك','خدمات واضحة وتفاصيل تساعدك')}<div class="cards-grid">{cards}</div>{related}</div></section>{contact_band()}</main>'''
    return head(title,desc,path,breadcrumb_schema([(name,path)]))+header()+content+footer()

def simple_page(kind):
    if kind=="about":
        title=f"من نحن | {NAME} بالرياض"; desc=f"تعرّف على {NAME}: خدمات سباكة وكهرباء وإنارة في مواقع العملاء داخل الرياض، بإدارة من حي المصيف دون استقبال العملاء في المقر."; path="/about/"
        body=f'''<span class="eyebrow">عن أبو محمد</span><h1>شغل البيت يبدأ من <span>تشخيص المشكلة</span></h1><p class="simple-lead">أبو محمد سباك وكهربائي يقدم خدمات السباكة والكهرباء والإنارة داخل مدينة الرياض. الموقع يساعدك تختار نوع العمل، وتعرف ما يشمله، وتتواصل مباشرة لوصف حالتك.</p><div class="simple-panels"><div><span class="panel-icon">{icon('drop',28)}</span><h2>السباكة</h2><p>من تسربات المياه والصرف والسخانات إلى صيانة التركيبات وتمديدات المياه المنزلية.</p><a href="/plumbing/">تصفح خدمات السباكة {icon('arrow',17)}</a></div><div><span class="panel-icon amber">{icon('bolt',28)}</span><h2>الكهرباء والإنارة</h2><p>فحص الأعطال والقواطع، وتجهيز النقاط الكهربائية، وتركيب الإنارة وصيانتها.</p><a href="/electrical/">تصفح خدمات الكهرباء {icon('arrow',17)}</a></div></div><h2>طريقة طلب الخدمة</h2><p>أخبرنا بنوع المشكلة والحي داخل الرياض. وإذا كان عندك صورة للمكان أو القطعة، أرسلها على واتساب حتى تكون التفاصيل أوضح. يتم تحديد نطاق العمل والقطع اللازمة بحسب الحالة قبل التنفيذ.</p>{ctas()}'''
    else:
        title=f"تواصل معنا | {NAME} بالرياض"; desc=f"بيانات {NAME} ومقر إدارة النشاط في حي المصيف بالرياض. الخدمة في موقع العميل دون استقبال في المقر. اتصال وواتساب: {PHONE}."; path="/contact/"
        body=f'''<span class="eyebrow">تواصل معنا</span><h1>احكِ لنا عن المشكلة، <span>ونبدأ من التفاصيل</span></h1><p class="simple-lead">إذا تحتاج سباكًا أو كهربائيًا داخل الرياض، اتصل مباشرة أو أرسل رسالة على واتساب فيها نوع الخدمة والحي وصورة إن توفرت.</p><div class="contact-choices"><a href="tel:{PHONE}" class="contact-choice">{icon('phone',29)}<span><small>رقم الاتصال</small><strong dir="ltr">{PHONE}</strong></span>{icon('arrow',21)}</a><a href="{wa_url()}" target="_blank" rel="noopener noreferrer" class="contact-choice wa-choice"><svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="/assets/whatsapp.svg#wa"/></svg><span><small>واتساب مباشر</small><strong dir="ltr">{PHONE}</strong></span>{icon('arrow',21)}</a></div><div class="contact-hint">{icon('pin',22)}<span><strong>نطاق الخدمة</strong>مدينة الرياض، المملكة العربية السعودية</span></div><h2>ماذا تذكر في رسالتك؟</h2><p>اذكر نوع العطل، الحي، وقت ملاحظتك للمشكلة، وهل توجد صورة أو فيديو قصير يوضحها. هذه التفاصيل تساعد على معرفة نوع الخدمة المطلوبة، لكن تحديد العمل والتكلفة النهائية يعتمد على حالة الموقع.</p><a class="text-link" href="/services/">استعرض الخدمات {icon('arrow',19)}</a>'''
    content=f'<main id="main">{breadcrumbs([("من نحن" if kind=="about" else "تواصل معنا",None)])}<section class="simple-hero"><div class="container simple-content">{body}{business_details()}</div></section>{contact_band()}</main>'
    return head(title,desc,path,breadcrumb_schema([("من نحن" if kind=="about" else "تواصل معنا",path)]))+header()+content+footer()

def write(path,content):
    dest=OUT/path
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(content,encoding="utf-8")

def main():
    OUT.mkdir(exist_ok=True)
    write(Path("index.html"),home())
    write(Path("services/index.html"),listing_page())
    for category in CATEGORIES:
        write(Path(category)/"index.html",listing_page(category))
    for s in SERVICES:
        write(Path("services")/s["slug"]/"index.html",service_page(s))
    for kind in ("about","contact"):
        write(Path(kind)/"index.html",simple_page(kind))
    paths=["/","/services/","/plumbing/","/electrical/","/about/","/contact/"]+[f'/services/{s["slug"]}/' for s in SERVICES]
    write(Path("robots.txt"),f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    write(Path("sitemap.xml"),'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{canonical(p)}</loc><lastmod>{LAST_UPDATED}</lastmod></url>\n' for p in paths)+'</urlset>\n')
    print(f"Built {len(paths)} pages for {SITE}")

if __name__=="__main__":
    main()
