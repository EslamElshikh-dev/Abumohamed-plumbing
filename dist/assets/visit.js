const visitForm = document.getElementById("visit-request");
const district = visitForm.elements.namedItem("district");
district.addEventListener("input", () => district.setCustomValidity(""));

visitForm.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!district.value.trim()) {
    district.setCustomValidity("اكتب اسم الحي داخل الرياض.");
    district.reportValidity();
    return;
  }
  const values = new FormData(visitForm);
  const message = [
    "هلا أبو محمد، أحتاج تنسيق زيارة منزلية.",
    "الخدمة: " + values.get("service"),
    "الحي: " + district.value.trim(),
  ];
  const time = values.get("preferredTime").trim();
  const details = values.get("details").trim();
  if (time) message.push("الوقت المفضّل: " + time);
  if (details) message.push("تفاصيل الطلب: " + details);
  const destination = new URL(visitForm.dataset.whatsapp);
  destination.searchParams.set("text", message.join("\n"));
  window.location.assign(destination.toString());
});

visitForm.hidden = false;
document.getElementById("visit-fallback").hidden = true;
