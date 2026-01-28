# ⚙️ Pekiştirmeli Öğrenme ortamını kurma

## 🎯 Bu görevin amacı

Pekiştirmeli Öğrenme için ayrı bir ortam kurma.

Bu ünitede birçok yeni pakete ihtiyacımız var. Bu paketlerden bazıları, bootcamp'in diğer bölümleri için ihtiyaç duyduğumuz paket sürümleriyle uyumlu değil.

Bu yüzden yeni bir sanal ortam kuracağız. Bu şekilde iki ayrı python ortamımız olacak ve paketlerimiz çakışmayacak. 🦾

Bu, projeleriniz için sık sık yapacağınız bir şeydir: özel sanal ortamlar oluşturmak.

## 🐍 Yeni bir sanal ortam oluşturma

🐍 Sanal ortamı oluştur

```bash
cd ~/code/{{local_path_to("06-Deep-Learning/08-GAN-and-RL/00-Reinforcement-Env")}}
cd .. # Ünitenin ana klasörüne git
python --version # Önce, aşağıdaki <YOUR_PYTHON_VERSION> için Python sürümünüzü kontrol edin (ör. 3.12.9)
pyenv virtualenv <YOUR_PYTHON_VERSION> reinforcement-env
pyenv local reinforcement-env
pip install --upgrade pip
```

Ardından, Terminal'inizin sağ tarafında `[🐍 reinforcement-env]` görüntülediğinden emin olun.

## 📦 Paketleri yükleme

Bu görevin klasörüne geri gidin:

Bu klasörde, bu ünitenin görevleri için tüm gereksinimleri içeren bir `requirements.txt` dosyası oluşturduk. Hepsini yüklemek için sadece `pip install` yapmamız yeterli:

```bash
pip install -r requirements.txt
```

Temel olarak şunları yüklüyoruz:
- Jupyter Notebook ve tüm bağımlılıkları
- Pandas ve NumPy gibi klasikler
- Pekiştirmeli öğrenme ortamları oluşturmak için `gymnasium`
- Pekiştirmeli öğrenme algoritmalarını çalıştırmak için `stable-baselines`
- Sonuçları kaydetmek için `tensorboard`

## ✅ Kurulumunuzu kontrol edin

```bash
make test
```

Her şey yolunda mı? Değilse, bir eğitmenden yardım isteyin.


## 🏁 Tamamlandı

Artık LLM'ler ile çalışmak için taze bir ortamınız var.

Her zaman `reinforcement-env` ortamını kullandığınızı kontrol etmeyi unutmayın. Özellikle VS Code kullanırken, bu yeni ortamı seçtiğinizden emin olun.
